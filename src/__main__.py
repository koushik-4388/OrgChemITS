from kivy.app import App
from kivy.uix.label import Label
from core.main import main

class OrgChemITSApp(App):
    def build(self):
        return Label(text = "lol")


if __name__ == "__main__" :
    OrgChemITSApp().run()

# testCompounds = [[[0,0,1,1],[1,1,2,2],[1,1,1,0],[1,0,3,2],[1,0,3,1]],[[0,0,1,1]],[[0,0,1,1],[2,0,1,1]],[[0,0,1,1],[2,0,1,1],[2,0,5,5]],[[0,0,1,1],[2,0,1,1],[2,0,5,5],[5,5,9,9]],[[0,0,1,1],[2,0,1,1],[2,0,5,5],[5,5,9,9],[6,7,9,9]],[[0,0,1,1],[2,0,1,1],[2,0,5,5],[5,5,9,9],[6,7,9,9],[5,5,12,12]],[[0,0,1,1],[2,0,1,1],[2,0,5,5],[5,5,9,9],[6,7,9,9],[5,5,12,12],[5,5,78,78]],[[0,0,1,0],[1,0,2,1],[2,1,2,2],[2,2,1,3],[2,2,3,3],[2,1,3,0],[3,0,4,1],[3,0,4,-1]]]

# for node in main.mainAlgo(testCompounds[len(testCompounds)-1]):
#     print(node.getCords())
#     x = node.getConnectedNodes()
#     for lol in x:
#         print(lol.getCords())
#     print("next node")

# # for test in testCompounds:
# #     print(main.mainAlgo(test))