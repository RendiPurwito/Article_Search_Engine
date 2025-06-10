import streamlit as st

class TreeNode:
    def __init__(self, keyword, title, link, category):
        self.keyword = keyword
        self.title = title
        self.link = link
        self.category = category
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, keyword, title, link, category):
        new_node = TreeNode(keyword, title, link, category)
        if not self.root:
            self.root = new_node
            return
        current = self.root
        while True:
            if keyword < current.keyword:
                if current.left:
                    current = current.left
                else:
                    current.left = new_node
                    return
            else:
                if current.right:
                    current = current.right
                else:
                    current.right = new_node
                    return

    def search(self, node, query):
        if not node:
            return []
        result = []
        if query in node.keyword.lower() or query in node.title.lower():
            result.append(node)
        result.extend(self.search(node.left, query))
        result.extend(self.search(node.right, query))
        return result

    def inorder(self, node, result):
        if node:
            self.inorder(node.left, result)
            result.append(node)
            self.inorder(node.right, result)

    def preorder(self, node, result):
        if node:
            result.append(node)
            self.preorder(node.left, result)
            self.preorder(node.right, result)

    def postorder(self, node, result):
        if node:
            self.postorder(node.left, result)
            self.postorder(node.right, result)
            result.append(node)

class ArticleSearchApp:
    def __init__(self):
        self.article_tree = BinarySearchTree()
        self.initialize_dataset()

    def initialize_dataset(self):
        articles = [
            {"keyword": "machine learning", "title": "Introduction to Machine Learning", "link": "https://www.ibm.com/cloud/learn/machine-learning", "category": "Machine Learning"},
            {"keyword": "machine learning", "title": "Neural Networks Explained", "link": "https://towardsdatascience.com/neural-networks-explained-9d2c987a7faa", "category": "Machine Learning"},
            {"keyword": "machine learning", "title": "Reinforcement Learning Basics", "link": "https://www.analyticsvidhya.com/blog/2018/11/reinforcement-learning-introduction/", "category": "Machine Learning"},
            {"keyword": "machine learning", "title": "Unsupervised Learning Techniques", "link": "https://scikit-learn.org/stable/modules/clustering.html", "category": "Machine Learning"},
            {"keyword": "machine learning", "title": "Support Vector Machines", "link": "https://www.csie.ntu.edu.tw/~cjlin/papers/guide/guide.pdf", "category": "Machine Learning"},
            {"keyword": "data science", "title": "Big Data and Data Science", "link": "https://www.dataversity.net/big-data-and-data-science-a-comprehensive-look/", "category": "Data Science"},
            {"keyword": "data science", "title": "Python for Data Science", "link": "https://realpython.com/python-data-science/", "category": "Data Science"},
            {"keyword": "data science", "title": "Data Visualization with Python", "link": "https://seaborn.pydata.org/", "category": "Data Science"},
            {"keyword": "data science", "title": "Data Cleaning Techniques", "link": "https://towardsdatascience.com/data-cleaning-techniques-using-python-99e3f4183a2a", "category": "Data Science"},
            {"keyword": "data science", "title": "Exploratory Data Analysis", "link": "https://www.geeksforgeeks.org/exploratory-data-analysis-in-python/", "category": "Data Science"},
            {"keyword": "deep learning", "title": "Introduction to Deep Learning", "link": "https://www.deeplearningbook.org/", "category": "Deep Learning"},
            {"keyword": "deep learning", "title": "Convolutional Neural Networks", "link": "https://towardsdatascience.com/cnns-explained-3a619c2f5d3b", "category": "Deep Learning"},
            {"keyword": "deep learning", "title": "Recurrent Neural Networks", "link": "https://colah.github.io/posts/2015-08-Understanding-LSTMs/", "category": "Deep Learning"},
            {"keyword": "deep learning", "title": "GANs for Beginners", "link": "https://machinelearningmastery.com/what-are-generative-adversarial-networks-gans/", "category": "Deep Learning"},
            {"keyword": "deep learning", "title": "Deep Reinforcement Learning", "link": "https://deepmind.com/research/highlighted-research/deep-reinforcement-learning", "category": "Deep Learning"},
            {"keyword": "artificial intelligence", "title": "AI in Healthcare", "link": "https://www.forbes.com/sites/forbestechcouncil/2021/11/08/how-ai-is-changing-healthcare/", "category": "Artificial Intelligence"},
            {"keyword": "artificial intelligence", "title": "Ethics in AI", "link": "https://www.turing.ac.uk/research/ethics-ai", "category": "Artificial Intelligence"},
            {"keyword": "artificial intelligence", "title": "AI for Autonomous Vehicles", "link": "https://www.nhtsa.gov/technology-innovation/automated-vehicles-safety", "category": "Artificial Intelligence"},
            {"keyword": "artificial intelligence", "title": "AI in Financial Services", "link": "https://www.mckinsey.com/industries/financial-services/our-insights/ai-in-financial-services", "category": "Artificial Intelligence"},
            {"keyword": "artificial intelligence", "title": "Natural Language Processing", "link": "https://www.datacamp.com/community/tutorials/natural-language-processing-python", "category": "Artificial Intelligence"},
        ]
        for article in articles:
            self.article_tree.insert(article["keyword"], article["title"], article["link"], article["category"])

    def run(self):
        st.title("Article Search Engine")

        traversal_method = st.selectbox("Traversal Method", ["Inorder", "Preorder", "Postorder"])
        query = st.text_input("Search for articles").strip().lower()

        if st.button("Search"):
            results = self.article_tree.search(self.article_tree.root, query)

            traversal_results = []
            if traversal_method == "Inorder":
                self.article_tree.inorder(self.article_tree.root, traversal_results)
            elif traversal_method == "Preorder":
                self.article_tree.preorder(self.article_tree.root, traversal_results)
            elif traversal_method == "Postorder":
                self.article_tree.postorder(self.article_tree.root, traversal_results)

            filtered_results = [node for node in traversal_results if query in node.keyword.lower() or query in node.title.lower()]

            if filtered_results:
                for node in filtered_results:
                    st.markdown(f"### [{node.title}]({node.link})")
                    st.write(f"**Keyword:** {node.keyword} | **Category:** {node.category}")
            else:
                st.write("No articles found.")

if __name__ == "__main__":
    app = ArticleSearchApp()
    app.run()
