from selenium import webdriver
from bs4 import BeautifulSoup
#from urllib3.exceptions import InsecureRequestWarning
import csv



class Professors:

    def __init__ (self, csis_professor_id = ""):
        self.csis_professor_id = csis_professor_id

    def requestHeaders(self):
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
		'Accept-Encoding': 'none',
		'Accept-Language': 'en-US,en;q=0.8',
		'Connection': 'keep-alive'}

        return headers

    def CSIS_professor(self):

        csisProfessors = []
        uniqueCsisProfessorsList = []
    
        url = 'https://banserv2.douglas.bc.ca/prod/bwysched.p_course_search?wsea_code=CRED&term_code=202030&session_id=6784192&sel_subj=dummy&sel_camp=dummy&sel_sess=dummy&sel_attr=dummy&sel_levl=dummy&sel_schd=dummy&sel_ptrm=dummy&sel_insm=dummy&sel_link=dummy&sel_wait=dummy&sel_day=dummy&sel_begin_hh=dummy&sel_begin_mi=dummy&sel_begin_am_pm=dummy&sel_end_hh=dummy&sel_end_mi=dummy&sel_end_am_pm=dummy&sel_instruct=dummy&sel_open=dummy&sel_resd=dummy&sel_resd=R&sel_subj=CSIS&sel_number=&sel_camp=&sel_sess=&sel_day=m&sel_day=t&sel_day=w&sel_day=r&sel_day=f&sel_day=s&sel_day=u&sel_instruct='

        driver = webdriver.Chrome(executable_path='./drivers/chromedriver')
        driver.get(url)
        soup = BeautifulSoup(driver.page_source,'html.parser')
        for a in soup.select('table')[3].select('tr')[1:]:
            rows = a.select('td:nth-child(13)')
            for a in rows:
                csisProfessors.append(a.get_text())
        
        
        uniqueCsisProfessorsList = list(set(csisProfessors))
        
        return uniqueCsisProfessorsList

    def convertCsv(self,proflist):
        with open('professor_data.txt','w') as data_file:
            wr = csv.writer(data_file, quoting= csv.QUOTE_ALL)
            wr.writerow(proflist)
        


    
    @staticmethod
    def run():
        professors = Professors()
        proflist = professors.CSIS_professor()
        professors.convertCsv(proflist)