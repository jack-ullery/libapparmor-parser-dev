import unittest
import sys

sys.path.append('../')
import apparmor.aa

#from apparmor.aa import parse_event

class Test(unittest.TestCase):

    def test_loadinclude(self):
        apparmor.aa.loadincludes()
    
        
    def test_parse_event(self):
        event = 'type=AVC msg=audit(1345027352.096:499): apparmor="ALLOWED" operation="rename_dest" parent=6974 profile="/usr/sbin/httpd2-prefork//vhost_balmar" name=2F686F6D652F7777772F62616C6D61722E646174616E6F766F322E64652F68747470646F63732F6A6F6F6D6C612F696D616765732F6B75656368656E2F666F746F20322E6A7067 pid=20143 comm="httpd2-prefork" requested_mask="wc" denied_mask="wc" fsuid=30 ouid=30'
        parsed_event = apparmor.aa.parse_event(event)
        print(parsed_event)
        
        event = 'type=AVC msg=audit(1322614912.304:857): apparmor="ALLOWED" operation="getattr" parent=16001 profile=74657374207370616365 name=74657374207370616365 pid=17011 comm="bash" requested_mask="r" denied_mask="r" fsuid=0 ouid=0'
        parsed_event = apparmor.aa.parse_event(event)
        print(parsed_event)
        
        event = 'type=AVC msg=audit(1322614918.292:4376): apparmor="ALLOWED" operation="file_perm" parent=16001 profile=74657374207370616365 name="/home/jj/.bash_history" pid=17011 comm="bash" requested_mask="w" denied_mask="w" fsuid=0 ouid=1000'
        parsed_event = apparmor.aa.parse_event(event)
        print(parsed_event)
        
        
    def test_modes_to_string(self):
        self.assertEqual(apparmor.aa.mode_to_str(32270), 'rwPCUx')
        
        MODE_TEST = {'x': apparmor.aa.AA_MAY_EXEC,
             'w': apparmor.aa.AA_MAY_WRITE,
             'r': apparmor.aa.AA_MAY_READ,
             'a': apparmor.aa.AA_MAY_APPEND,
             'l': apparmor.aa.AA_MAY_LINK,
             'k': apparmor.aa.AA_MAY_LOCK,
             'm': apparmor.aa.AA_EXEC_MMAP,
             'i': apparmor.aa.AA_EXEC_INHERIT,
             'u': apparmor.aa.AA_EXEC_UNCONFINED + apparmor.aa.AA_EXEC_UNSAFE,  # Unconfined + Unsafe
              'U': apparmor.aa.AA_EXEC_UNCONFINED,
              'p': apparmor.aa.AA_EXEC_PROFILE + apparmor.aa.AA_EXEC_UNSAFE,    # Profile + unsafe
              'P': apparmor.aa.AA_EXEC_PROFILE,
              'c': apparmor.aa.AA_EXEC_CHILD + apparmor.aa.AA_EXEC_UNSAFE,  # Child + Unsafe
              'C': apparmor.aa.AA_EXEC_CHILD,
              #'n': AA_EXEC_NT + AA_EXEC_UNSAFE,
              #'N': AA_EXEC_NT
              }
        
        while MODE_TEST:
            string,mode = MODE_TEST.popitem()
            self.assertEqual(apparmor.aa.mode_to_str(mode), string)
            
        mode = 2048
        self.assertEqual(apparmor.aa.mode_to_str(mode), 'C')
        
    def test_string_to_modes(self):

        #self.assertEqual(apparmor.aa.str_to_mode('wc'), 32270)

        MODE_TEST = {'x': apparmor.aa.AA_MAY_EXEC,
             'w': apparmor.aa.AA_MAY_WRITE,
             'r': apparmor.aa.AA_MAY_READ,
             'a': apparmor.aa.AA_MAY_APPEND,
             'l': apparmor.aa.AA_MAY_LINK,
             'k': apparmor.aa.AA_MAY_LOCK,
             'm': apparmor.aa.AA_EXEC_MMAP,
             'i': apparmor.aa.AA_EXEC_INHERIT,
             'u': apparmor.aa.AA_EXEC_UNCONFINED + apparmor.aa.AA_EXEC_UNSAFE,  # Unconfined + Unsafe
              'U': apparmor.aa.AA_EXEC_UNCONFINED,
              'p': apparmor.aa.AA_EXEC_PROFILE + apparmor.aa.AA_EXEC_UNSAFE,    # Profile + unsafe
              'P': apparmor.aa.AA_EXEC_PROFILE,
              'c': apparmor.aa.AA_EXEC_CHILD + apparmor.aa.AA_EXEC_UNSAFE,  # Child + Unsafe
              'C': apparmor.aa.AA_EXEC_CHILD,
              #'n': AA_EXEC_NT + AA_EXEC_UNSAFE,
              #'N': AA_EXEC_NT
              }
        
        #while MODE_TEST:
        #    string,mode = MODE_TEST.popitem()
        #    self.assertEqual(apparmor.aa.str_to_mode(string), mode)
            
        #self.assertEqual(apparmor.aa.str_to_mode('C'), 2048)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()