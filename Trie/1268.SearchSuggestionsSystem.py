class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        searchInput = ''
        res = []

        for char in searchWord:
            searchInput += char
            n = len(products)
            temp = []

            for product in products:
                if product.startswith(searchInput):
                    temp.append(product)
                
                
            products = temp
            res.append(products[:3])
            
        return res

# Time: O(n^2)
# Space: O(1)