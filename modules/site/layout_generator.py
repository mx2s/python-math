class LayoutGenerator:
    @staticmethod
    def gen_header():
        """
        :return:
        """
        return "<center>" \
               "<a href='/'><h1>Python-math</h1></a>" \
               "<h3>My study project, using numpy & other math stuff</h3>" \
               "</center>"

    @staticmethod
    def gen_title(content):
        """
        :param content:
        :return:
        """
        return "<center><i><h3>" + str(content) + "</h3></i></center>"
