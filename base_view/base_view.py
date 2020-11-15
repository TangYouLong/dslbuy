class BaseView(object):
    def __init__(self,driver):
        self.driver=driver

    def find_element(self,*loc):
        return self.driver.find_element(*loc)

    def find_elements(self,*loc):
        return self.driver.find_elements(*loc)

    def get_window_size(self):
        return self.driver.get_window_size()


    def tap(self,positons,duration=None):
        return self.driver.tap(positions,duration=None)

    # def touch_action(self):
    #     return self.driver.tap()

    # def tap(self,element=None,x=None,y=None,count=1):
    #     return self.driver.tap(element=None,x=None,y=None,count=1)

        # return self.driver.common.touch_action.TouchAction(self.driver).Tap(element)

    def swipe(self,start_x,start_y,end_x,end_y,duration):
        return self.driver.swipe(start_x,start_y,end_x,end_y,duration)
