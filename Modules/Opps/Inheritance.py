import os

class Tomcat(object):
    def get_home_conf_file(self,server_xml):
        self.t_home=os.path.dirname(os.path.dirname(server_xml))
        self.conf_file=server_xml
    def display_details(self):
        print("Tomcat home is",self.t_home)
        print("Tomcat config file",self.conf_file)
def get_all_tomcats():
    list_of_config_files=[]
    for r,d,f in os.walk("/"):
        for each_file in f:
            if each_file == 'server.xml':
                list_of_config_files.append(os.path.join(r,each_file))
    return list_of_config_files
def main():
    print("Finding list of Tomcats")
    list_of_tomcats=get_all_tomcats()
    tomcat_objects=[]
    for each_file in list_of_tomcats:
        tomcat_object=Tomcat()
        tomcat_object.get_home_conf_file(each_file)
        tomcat_objects.append(tomcat_object)
    for each_obj in tomcat_objects:
        each_obj.display_details()   
    return None
if __name__ == '__main__':
    main()

