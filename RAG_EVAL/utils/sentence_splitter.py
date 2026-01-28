import re
class TextSplitter:
    def split_text(self, text:str):
        splitted_strs = re.split(r'[.!?]\s*', text)
        return [splitted.strip() for splitted in splitted_strs]

# splitter = TextSplitter()
# print(splitter.split_text("Хело. Ворлд"))