from lib import AngQuick

def start():
    aq = AngQuick()
    aq.check_posix()
    component_name = aq.prompt()
    aq.gen_new_component_files(component_name)

# call start()
start()