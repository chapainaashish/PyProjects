
# Search engine


def search(user_search, user_list):
    """Take search keyword and list then return the most occurred element in descending order """
    import re
    result_list = []
    for element in user_list:
        try:
            # search keyword inside element
            # this will return list with repeated keyword
            result = re.findall(user_search, element, re.IGNORECASE)

        except:
            raise ValueError("Inappropriate keyword passed")
        else:

            # count searched keyword length
            result_count = len(result)

            # to clear previous content and to save only statement and searched keyword len
            result.clear()

            # if search result keyword is 0 why waste time to save it when not 0
            if result_count != 0:
                result.append(result_count)
                result.append(element)
                result_list.append(result)
    sorted_list = sorted(result_list, key=lambda x: x[0], reverse=True)

    # 'sorted_list' is list of list
    return sorted_list
