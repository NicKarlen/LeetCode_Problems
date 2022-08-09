class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        for i in image:
            print(i)
        print('\n')

        if image[sr][sc] == color:
            return image

        from collections import deque
        nodedeque = deque([[sr,sc]])
        startingColor = image[sr][sc]
        image[sr][sc] = color

        while nodedeque:

            cur = nodedeque.popleft()
            if cur[0] > 0:
                if image[cur[0] - 1][cur[1]] == startingColor:
                    nodedeque.append([cur[0] - 1, cur[1]])
                    image[cur[0] - 1][cur[1]] = color

            if cur[0] < len(image)-1:
                if image[cur[0] + 1][cur[1]]== startingColor:
                    nodedeque.append([cur[0] + 1, cur[1]])
                    image[cur[0] + 1][cur[1]] = color

            if cur[1] > 0:
                if image[cur[0]][cur[1] - 1]== startingColor:
                    nodedeque.append([cur[0], cur[1] - 1])
                    image[cur[0]][cur[1] - 1] = color

            if cur[1] < len(image[0])-1:
                if image[cur[0]][cur[1] + 1]== startingColor:
                    nodedeque.append([cur[0], cur[1] + 1])
                    image[cur[0]][cur[1] + 1] = color

            for i in image:
                print(i)
            print('\n')


        return image


sl = Solution()


#sl.floodFill([[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2)

sl.floodFill([[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0)