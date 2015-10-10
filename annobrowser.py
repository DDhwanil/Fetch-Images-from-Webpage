import mechanize, cookielib,random
class annobrowser(mechanize.Browser):
    
    def __init__(self,proxies=[],user_agents=[]):
        mechanize.Browser.__init__(self)
        self.set_handle_robots(False)
        self.proxies=proxies
        self.user_agents=user_agents+['Mozila/32.0','firefox/5.0','ExactSearch']
        self.cookie_jar=cookielib.LWPCookieJar()
        self.set_cookiejar(self.cookie_jar)
        self.anonymize()

    def clear_cookies(self):
        self.cookie_jar=cookielib.LWPCookieJar()
        self.set_cookiejar(self.cookie_jar)

    def change_user_agents(self):
        index=random.randrange(0,len(self.user_agents))
        self.addheader=[('User-agent'),(self.user_agents[index])]

    def change_proxy(self):
        if self.proxies:
            index=random.randrange(0,len(self.proxies))
            self.set_proxies({'http':self.proxies[index]})

    def anonymize(self,sleep=False):
        self.clear_cookies()
        self.change_user_agents()
        self.change_proxy()
        if sleep:
            time.sleep(5)
