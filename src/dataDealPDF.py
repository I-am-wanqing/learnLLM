from langchain_learn.document_loaders.pdf import PyMuPDFLoader

# 创建一个 PyMuPDFLoader Class 实例，输入为待加载的 pdf 文档路径
loader = PyMuPDFLoader("../data_base/knowledge_db/pumkin_book/pumpkin_book.pdf")

# 调用 PyMuPDFLoader Class 的函数 load 对 pdf 文件进行加载
pdf_pages = loader.load()

import re





if __name__ == '__main__':
    print(f"载入后的变量类型为：{type(pdf_pages)}，", f"该 PDF 一共包含 {len(pdf_pages)} 页")
    pdf_page = pdf_pages[1]
    print(f"每一个元素的类型：{type(pdf_page)}.",
          f"该文档的描述性数据：{pdf_page.metadata}",
          f"查看该文档的内容:\n{pdf_page.page_content}",
          sep="\n------\n")
    pattern = re.compile(r'[^\u4e00-\u9fff](\n)[^\u4e00-\u9fff]', re.DOTALL)
    pdf_page.page_content = re.sub(pattern, lambda match: match.group(0).replace('\n', ''), pdf_page.page_content)
    print(pdf_page.page_content)
    pdf_page.page_content = pdf_page.page_content.replace('•', '')
    pdf_page.page_content = pdf_page.page_content.replace(' ', '')
    print(pdf_page.page_content)



