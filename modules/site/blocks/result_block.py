from modules.site.layout_generator import LayoutGenerator


class ResultBlock:
    title = ""
    table_columns = []
    table_data = []

    def __init__(self):
        self.table_data = []

    def render(self):
        content = LayoutGenerator.gen_title(self.title)
        content += "<center><table border='1' cellpadding='2'><tr>"
        for column in self.table_columns:
            content += "<th>{0}</th>".format(str(column))
        content += "</tr>"
        for row in self.table_data:
            content += "<tr>"
            for cell in row:
                content += "<td>{0}</td>".format(str(cell))
            content += "</tr>"
        return content + "</table></center>"
