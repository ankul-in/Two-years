#kata
#https://www.codewars.com/kata/54eecc187f9142cc4600119e/train/python

class HTMLGen:
    def __init__(self):
        pass
    def a(self,var):
        return f"<a>{var}</a>"
    def b(self,var):
        return f"<b>{var}</b>"
    def p(self,var):
        return f"<p>{var}</p>"
    def body(self,var):
        return f"<body>{var}</body>"
    def div(self,var):
        return f"<div>{var}</div>"
    def span(self,var):
        return f"<span>{var}</span>"
    def title(self,var):
        return f"<title>{var}</title>"
    def comment(self,var):
        return f"<!--{var}-->"
    



class HTMLGen:
    def __init__(self):
        self.a = lambda t: self.tag("a", t)
        self.b = lambda t: self.tag("b", t)
        self.p = lambda t: self.tag("p", t)
        self.body = lambda t: self.tag("body", t)
        self.div = lambda t: self.tag("div", t)
        self.span = lambda t: self.tag("span", t)
        self.title = lambda t: self.tag("title", t)
        
    def tag(self, tag_str, content):
        return "<{}>{}</{}>".format(tag_str, content, tag_str)
        
    def comment(self, content):
        return "<!--{}-->".format(content)