class List(object):
    def count_spec_digits(self, integers_list, digits_list):
        int_list = "".join(map(str, integers_list))
        result = []
        for num in digits_list:
            result.append((num, int_list.count(str(num))))
        return result
