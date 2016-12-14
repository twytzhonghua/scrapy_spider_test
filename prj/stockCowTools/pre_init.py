
import update_stock


def init_stock_number():
    stock_list = update_stock.update_all_stock_number()
    return stock_list


def inityidianGDURLS():
    stock_list = init_stock_number()
    update_stock.generateYiDianGDUrls(stock_list)
    
if __name__ == "__main__":
    inityidianGDURLS()