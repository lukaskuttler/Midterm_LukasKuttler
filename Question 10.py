def is_valid_url(url):
    # a basic valid URL should start with http:// or https://
    if url[:7] == "http://" or url[:8] == "https://":

        # remove the protocol part
        if url[:7] == "http://":
            rest = url[7:]
        else:
            rest = url[8:]

        # a valid domain must contain at least one dot
        if "." in rest:
            parts = rest.split(".")

            # make sure no part of the domain is empty
            for part in parts:
                if len(part) == 0:
                    return False

            return True

    return False


print(is_valid_url("https://www.google.com"))
print(is_valid_url("google.com"))