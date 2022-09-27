from typing import Optional, List, Dict, Any

class UserLevelTable:
    '''
    Stores the User level table as a dict.
    '''
    table = {
        2700:1,
        6050:2,
        9950:3,
        14300:4,
        19100:5,
        24350:6,
        30050:7,
        36650:8,
        51250:9,
        58300:10,
        65800:11,
        73750:12,
        82150:13,
        91000:14,
        100300:15,
        110050:16,
        120700:17,
        133150:18,
        154600:19,
        167950:20,
        182200:21,
        197350:22,
        213400:23,
        230350:24,
        248200:25,
        266950:26,
        287500:27,
        311650:28,
        353800:29,
        379300:30,
        406150:31,
        434350:32,
        463900:33,
        494800:34,
        527050:35,
        560650:36,
        596950:37,
        638650:38,
        707350:39,
        750850:40,
        796150:41,
        843250:42,
        892150:43,
        942850:44,
        995350:45,
        1049650:46,
        1107550:47,
        1172650:48,
        1273750:49,
        1341100:50,
        1410700:51,
        1482550:52,
        1556650:53,
        1633000:54,
        1711600:55,
        1792450:56,
        1877800:57,
        1972150:58,
        2111500:59,
        2208550:60,
        2308300:61,
        2410750:62,
        2515900:63,
        2623750:64,
        2734300:65,
        2847550:66,
        2963500:67,
        3084850:68,
        3260200:69,
        3384700:70,
        3512350:71,
        3643150:72,
        3777100:73,
        3914200:74,
        4054450:75,
        4197850:76,
        4347550:77,
        4509850:78,
        4735150:79,
        4904650:80,
        5081450:81,
        5265650:82,
        5457350:83,
        5656650:84,
        5863650:85,
        6078450:86,
        6301150:87,
        6539650:88,
        6850150:89,
        7100800:90,
        7364100:91,
        7640550:92,
        7930650:93,
        8234900:94,
        8553800:95,
        8887850:96,
        9252200:97,
        9697550:98,
        9697550:99,
    }

class ValidatedDict(dict):
    """
    Helper class which gives a Dict object superpowers. Allows stores and loads to be
    validated so you only ever update when given good data, and only ever return
    non-default values when data is good. Used primarily for storing data pulled
    directly from game responses, or reading data to echo to a game.

    All of the get functions will verify that the attribute exists and is the right
    type. If it is not, the default value is returned.

    all of the set functions will verify that the to-be-stored value matches the
    type. If it does not, the value is not updated.
    """

    def get_int(self, name: str, default: int=0) -> int:
        """
        Given the name of a value, return an integer stored under that name.

        Parameters:
            name - Name of attribute
            default - The default to return if the value doesn't exist, or isn't an integer.

        Returns:
            An integer.
        """
        val = self.get(name)
        if val is None:
            return default
        if type(val) != int:
            return default
        return val

    def get_float(self, name: str, default: float=0.0) -> float:
        """
        Given the name of a value, return a float stored under that name.

        Parameters:
            name - Name of attribute
            default - The default to return if the value doesn't exist, or isn't a float.

        Returns:
            A float.
        """
        val = self.get(name)
        if val is None:
            return default
        if type(val) != float:
            return default
        return val

    def get_bool(self, name: str, default: bool=False) -> bool:
        """
        Given the name of a value, return a boolean stored under that name.

        Parameters:
            name - Name of attribute
            default - The default to return if the value doesn't exist, or isn't a boolean.

        Returns:
            A boolean.
        """
        val = self.get(name)
        if val is None:
            return default
        if type(val) != bool:
            return default
        return val

    def get_str(self, name: str, default: str='') -> str:
        """
        Given the name of a value, return string stored under that name.

        Parameters:
            name - Name of attribute
            default - The default to return if the value doesn't exist, or isn't a string.

        Returns:
            A string.
        """
        val = self.get(name)
        if val is None:
            return default
        if type(val) != str:
            return default
        return val

    def get_bytes(self, name: str, default: bytes=b'') -> bytes:
        """
        Given the name of a value, return bytes stored under that name.

        Parameters:
            name - Name of attribute
            default - The default to return if the value doesn't exist, or isn't bytes.

        Returns:
            A bytestring.
        """
        val = self.get(name)
        if val is None:
            return default
        if type(val) != bytes:
            return default
        return val

    def get_int_array(self, name: str, length: int, default: Optional[List[int]]=None) -> List[int]:
        """
        Given the name of a value, return a list of integers stored under that name.

        Parameters:
            name - Name of attribute
            length - The expected length of the array
            default - The default to return if the value doesn't exist, or isn't a list of integers
                      of the right length.

        Returns:
            A list of integers.
        """
        if default is None:
            default = [0] * length
        if len(default) != length:
            raise Exception('Gave default of wrong length!')

        val = self.get(name)
        if val is None:
            return default
        if type(val) != list:
            return default
        if len(val) != length:
            return default
        for v in val:
            if type(v) != int:
                return default
        return val

    def get_bool_array(self, name: str, length: int, default: Optional[List[bool]]=None) -> List[bool]:
        """
        Given the name of a value, return a list of booleans stored under that name.

        Parameters:
            name - Name of attribute
            length - The expected length of the array
            default - The default to return if the value doesn't exist, or isn't a list of booleans
                      of the right length.

        Returns:
            A list of booleans.
        """
        if default is None:
            default = [False] * length
        if len(default) != length:
            raise Exception('Gave default of wrong length!')

        val = self.get(name)
        if val is None:
            return default
        if type(val) != list:
            return default
        if len(val) != length:
            return default
        for v in val:
            if type(v) != bool:
                return default
        return val

    def get_bytes_array(self, name: str, length: int, default: Optional[List[bytes]]=None) -> List[bytes]:
        """
        Given the name of a value, return a list of bytestrings stored under that name.

        Parameters:
            name - Name of attribute
            length - The expected length of the array
            default - The default to return if the value doesn't exist, or isn't a list of bytestrings
                      of the right length.

        Returns:
            A list of bytestrings.
        """
        if default is None:
            default = [b''] * length
        if len(default) != length:
            raise Exception('Gave default of wrong length!')

        val = self.get(name)
        if val is None:
            return default
        if type(val) != list:
            return default
        if len(val) != length:
            return default
        for v in val:
            if type(v) != bytes:
                return default
        return val

    def get_str_array(self, name: str, length: int, default: Optional[List[str]]=None) -> List[str]:
        """
        Given the name of a value, return a list of strings stored under that name.

        Parameters:
            name - Name of attribute
            length - The expected length of the array
            default - The default to return if the value doesn't exist, or isn't a list of strings
                      of the right length.

        Returns:
            A list of strings.
        """
        if default is None:
            default = [''] * length
        if len(default) != length:
            raise Exception('Gave default of wrong length!')

        val = self.get(name)
        if val is None:
            return default
        if type(val) != list:
            return default
        if len(val) != length:
            return default
        for v in val:
            if type(v) != str:
                return default
        return val

    def get_dict(self, name: str, default: Optional[Dict[Any, Any]]=None) -> 'ValidatedDict':
        """
        Given the name of a value, return a dictionary stored under that name.

        Parameters:
            name - Name of attribute
            default - The default to return if the value doesn't exist, or isn't a dictionary.

        Returns:
            A dictionary, wrapped with this helper class so the same helper methods may be called.
        """
        if default is None:
            default = {}
        validateddefault = ValidatedDict(default)

        val = self.get(name)
        if val is None:
            return validateddefault
        if not isinstance(val, dict):
            return validateddefault
        return ValidatedDict(val)

    def replace_int(self, name: str, val: Any) -> None:
        """
        Given the name of a value and a new value to store, update that value.

        Parameters:
            name - Name of attribute
            val - The value to store, if it is actually an integer.
        """
        if val is None:
            return
        if type(val) != int:
            return
        self[name] = val

    def replace_float(self, name: str, val: Any) -> None:
        """
        Given the name of a value and a new value to store, update that value.

        Parameters:
            name - Name of attribute
            val - The value to store, if it is actually a float
        """
        if val is None:
            return
        if type(val) != float:
            return
        self[name] = val

    def replace_bool(self, name: str, val: Any) -> None:
        """
        Given the name of a value and a new value to store, update that value.

        Parameters:
            name - Name of attribute
            val - The value to store, if it is actually a boolean.
        """
        if val is None:
            return
        if type(val) != bool:
            return
        self[name] = val

    def replace_str(self, name: str, val: Any) -> None:
        """
        Given the name of a value and a new value to store, update that value.

        Parameters:
            name - Name of attribute
            val - The value to store, if it is actually a string.
        """
        if val is None:
            return
        if type(val) != str:
            return
        self[name] = val

    def replace_bytes(self, name: str, val: Any) -> None:
        """
        Given the name of a value and a new value to store, update that value.

        Parameters:
            name - Name of attribute
            val - The value to store, if it is actually a bytestring.
        """
        if val is None:
            return
        if type(val) != bytes:
            return
        self[name] = val

    def replace_int_array(self, name: str, length: int, val: Any) -> None:
        """
        Given the name of a value and a new value to store, update that value.

        Parameters:
            name - Name of attribute
            length - Expected length of the list
            val - The value to store, if it is actually a list of integers containing length elements.
        """
        if val is None:
            return
        if type(val) != list:
            return
        if len(val) != length:
            return
        for v in val:
            if type(v) != int:
                return
        self[name] = val

    def replace_bool_array(self, name: str, length: int, val: Any) -> None:
        """
        Given the name of a value and a new value to store, update that value.

        Parameters:
            name - Name of attribute
            length - Expected length of the list
            val - The value to store, if it is actually a list of booleans containing length elements.
        """
        if val is None:
            return
        if type(val) != list:
            return
        if len(val) != length:
            return
        for v in val:
            if type(v) != bool:
                return
        self[name] = val

    def replace_bytes_array(self, name: str, length: int, val: Any) -> None:
        """
        Given the name of a value and a new value to store, update that value.

        Parameters:
            name - Name of attribute
            length - Expected length of the list
            val - The value to store, if it is actually a list of bytestrings containing length elements.
        """
        if val is None:
            return
        if type(val) != list:
            return
        if len(val) != length:
            return
        for v in val:
            if type(v) != bytes:
                return
        self[name] = val

    def replace_str_array(self, name: str, length: int, val: Any) -> None:
        """
        Given the name of a value and a new value to store, update that value.

        Parameters:
            name - Name of attribute
            length - Expected length of the list
            val - The value to store, if it is actually a list of strings containing length elements.
        """
        if val is None:
            return
        if type(val) != list:
            return
        if len(val) != length:
            return
        for v in val:
            if type(v) != str:
                return
        self[name] = val

    def replace_dict(self, name: str, val: Any) -> None:
        """
        Given the name of a value and a new value to store, update that value.

        Parameters:
            name - Name of attribute
            val - The value to store, if it is actually a dictionary.
        """
        if val is None:
            return
        if not isinstance(val, dict):
            return
        self[name] = val

    def increment_int(self, name: str) -> None:
        """
        Given the name of a value, increment the value by 1.

        If the value doesn't exist or isn't an integer, converts it to an integer
        and sets it to 1 (as if it was 0 before). If it is an integer, increments
        it by 1.

        Parameters:
            name - Name of attribute
        """
        if name not in self:
            self[name] = 1
        elif type(self[name]) != int:
            self[name] = 1
        else:
            self[name] = self[name] + 1
