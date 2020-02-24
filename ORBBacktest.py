#!/usr/local/bin/python

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import json
import pdb
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class ZerodhaSelenium( object ):

   def __init__( self ):
      self.timeout = 5
      self.loadCredentials()
      self.driver = webdriver.Chrome()

   def getCssElement( self, cssSelector ):
      '''
      To make sure we wait till the element appears
      '''
      return WebDriverWait( self.driver, self.timeout ).until( EC.presence_of_element_located( ( By.CSS_SELECTOR, cssSelector ) ) )

   def loadCredentials( self ):
      self.username = "FA15897"
      self.password = "Finvasia@13"
      self.security = "123456"
      self.fieldanswer1="1"
      self.fieldanswer2="1"

   def doLogin( self ):
      #let's login
      self.driver.get( "https://trade.finvasia.com/")
      try:
         passwordField = self.getCssElement( "input[placeholder=Password]" )
         print(passwordField)
         passwordField.send_keys( self.password )
         userNameField = self.getCssElement( "input[placeholder='Client Code']" )
         print(userNameField)
         userNameField.send_keys( self.username )
         loginButton = self.getCssElement( "button[class='login_btn pull-left']" )
         loginButton.click()

         # 2FA
         # form2FA = self.getCssElement( "form.form-control" )
         # fieldQuestion1 = form2FA.find_element_by_css_selector( "div:nth-child(2) > div > label.accordin_txtin")
         # fieldQuestion2 = form2FA.find_element_by_css_selector( "div:nth-child(3) > div > label.accordin_txtin")
         fieldAnswer1 = self.getCssElement( "input[class='form-control accordin_txtin']" )
         # print("This is an \"escape\" of a double-quote")
         # fieldAnswer2 = self.getCssElement('div.form-control accordin_txtin:nth-of-type(2)');
         
         fieldAnswer1.send_keys( self.fieldanswer1 )
         fieldAnswer1.send_keys(Keys.TAB,self.fieldanswer2,Keys.TAB,Keys.ENTER)
		 
         # stock1 = self.find_element_by_css_selector( "/html/body/div/div[1]/div/div/div/div[1]/div[2]/div/table/tbody/tr[4]" ).click()
         # stock1=self.driver.find_element_by_xpath("/html/body/div/div[1]/div/div/div/div[3]/div/div[2]/ul/li[2]/a").click()

         # buttonSubmit.click()
		 
         
         
      except TimeoutException:
         print( "Timeout occurred" )

      pdb.set_trace()
      # close chrome
      self.driver.quit()

if __name__ == "__main__":
   obj = ZerodhaSelenium()
   obj.doLogin()
