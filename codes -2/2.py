
class ReportGenerator:
    def generate_report(self, data):
        return f"Report: {data}"

class ReportSaver:
    def save_to_file(self, report, filename):
        with open(filename, 'w') as file:
            file.write(report)

data = "Sales Data"
report = ReportGenerator().generate_report(data)
ReportSaver().save_to_file(report, "report.txt")