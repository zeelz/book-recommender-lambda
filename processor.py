def getBooks(category, book_list):
        if(category == "ai" or category == "ml"):
            return book_list["ai-ml"]
        elif (category == "cloud" or category == "serverless"):
               return book_list["cloud-serverless"]
        elif (category == "sales"):
               return book_list["marketing"]
        return book_list[category]
        


