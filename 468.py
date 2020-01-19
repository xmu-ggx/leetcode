
class Solution:
    def validIPAddress(self, IP):
        if self.isIPv4(IP):
            return 'IPv4'

        if self.isIPv6(IP):
            return 'IPv6'

        return 'Neither'

    def isIPv4(self, IP):
        if '.' in IP:
            ll = IP.split('.')
            if len(ll) != 4: return False
            for item in ll:
                try:
                    temp = int(item)
                except ValueError:
                    return False
                else:
                    if temp < 0 or temp > 255:
                        return False
                    if item != str(temp):
                        return False
            return True

    def isIPv6(self, IP):
        ipv6_list = [str(i) for i in range(10)] + [chr(i) for i in range(65, 71)] + [chr(i) for i in range(97, 103)]
        if ':' in IP:
            ll = IP.split(':')
            if len(ll) != 8: return False
            for item in ll:
                if len(item) > 4 or len(item) == 0: return False
                for s in item:
                    if s not in ipv6_list:
                        return False
            return True

