class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if len(intervals) < 2:
            return 0
        self.intervals = []
        all_intv_str = []
        for intv in intervals:
            intv_str = str(intv[0]) + ',' + str(intv[1])
            if intv_str not in all_intv_str:
                self.intervals.append(intv)
            all_intv_str.append(intv_str)
        self.repeat_count = len(intervals) - len(self.intervals)
        self.intervals.sort(key=lambda x:x[0])
        max_non_overlap = self.maxNonOverlapIntervalRecursive(self.intervals)
        self.remove_count = len(self.intervals) - max_non_overlap
        res = self.repeat_count + self.remove_count
        return res

    def maxNonOverlapIntervalRecursive(self, intervals):
        if len(intervals) < 2:
            return len(intervals)
        if len(intervals) == 2:
            return 1 if self.isOverlap(intervals[0], intervals[1]) else 2
        interval_left, interval_mid, interval_right = self.separateToNonOverlap(intervals)
        left_res = self.maxNonOverlapIntervalRecursive(interval_left)
        right_res = self.maxNonOverlapIntervalRecursive(interval_right)
        res_no_mid = left_res + right_res
        if len(interval_mid) == 0:
            return res_no_mid
        res_with_mid = []
        for intv in interval_mid:
            interval_left_temp = self.removeOverlapped(interval_left, intv, from_right=True)
            interval_right_temp = self.removeOverlapped(interval_right, intv, from_right=False)
            if len(interval_left_temp) < interval_left:
                left_res_with_mid = self.maxNonOverlapIntervalRecursive(interval_left_temp)
            else:
                left_res_with_mid = left_res
            if len(interval_right_temp) < interval_right:
                right_res_with_mid = self.maxNonOverlapIntervalRecursive(interval_right_temp)
            else:
                right_res_with_mid = right_res
            res_with_mid.append(1 + left_res_with_mid + right_res_with_mid)
        return max(res_no_mid, max(res_with_mid))

    def removeOverlapped(self, intervals, intv, from_right):
        if len(intervals) == 0:
            return intervals
        if from_right:
            intervals_new = []
            for i in intervals:
                if not self.isOverlap(i, intv):
                    intervals_new.append(i)
            return intervals_new
        else:
            i = 0
            while intervals[i][0] < intv[1]:
                i += 1
                if i == len(intervals):
                    return []
            return intervals[i:]

    def separateToNonOverlap(self, intervals):
        pivot = self.getPivot(intervals)
        left_id = len(intervals) / 2
        while intervals[left_id][1] > pivot:
            left_id -= 1
            if left_id == -1:
                break
        if left_id == -1:
            interval_left = []
        else:
            interval_left = intervals[:left_id+1]

        right_id = len(intervals) / 2
        while intervals[right_id][0] < pivot:
            right_id += 1
            if right_id == len(intervals):
                break

        if right_id == len(intervals):
            interval_right = []
        else:
            interval_right = intervals[right_id:]

        interval_mid = intervals[left_id+1:right_id]

        return interval_left, interval_mid, interval_right

    def getMinStart(self, intervals):
        return min([i[0] for i in intervals])

    def getMaxEnd(self, intervals):
        return max([i[1] for i in intervals])

    def getPivot(self, intervals):
        mid_intv = intervals[len(intervals) / 2]
        return (mid_intv[0] + mid_intv[1]) / 2

    def isOverlap(self, a, b):
        return a[1] > b[0] and a[0] < b[1]

test = Solution()
print test.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]) # 1
print test.eraseOverlapIntervals([[1,2],[1,2],[1,2]]) # 2
print test.eraseOverlapIntervals([[1,2],[2,3]]) # 0
print test.eraseOverlapIntervals([[1,2]]) # 0
print test.eraseOverlapIntervals([]) # 0
print test.eraseOverlapIntervals([[1,2],[1,2],[1,2],[1,4],[1,4],[1,4]]) # 5
print test.eraseOverlapIntervals([[1,100],[11,22],[1,11],[2,12]]) # 2
print test.eraseOverlapIntervals([[0,2],[1,3],[2,4],[3,5],[4,6]]) # 2
print test.eraseOverlapIntervals([[0,2],[1,3],[1,3],[2,4],[3,5],[3,5],[4,6]]) # 4
print test.eraseOverlapIntervals(
    [[-100,-87],[-99,-44],[-98,-19],[-97,-33],[-96,-60],[-95,-17],[-94,-44],[-93,-9],[-92,-63],[-91,-76],[-90,-44],[-89,-18],[-88,10],[-87,-39],[-86,7],[-85,-76],[-84,-51],[-83,-48],[-82,-36],[-81,-63],[-80,-71],[-79,-4],[-78,-63],[-77,-14],[-76,-10],[-75,-36],[-74,31],[-73,11],[-72,-50],[-71,-30],[-70,33],[-69,-37],[-68,-50],[-67,6],[-66,-50],[-65,-26],[-64,21],[-63,-8],[-62,23],[-61,-34],[-60,13],[-59,19],[-58,41],[-57,-15],[-56,35],[-55,-4],[-54,-20],[-53,44],[-52,48],[-51,12],[-50,-43],[-49,10],[-48,-34],[-47,3],[-46,28],[-45,51],[-44,-14],[-43,59],[-42,-6],[-41,-32],[-40,-12],[-39,33],[-38,17],[-37,-7],[-36,-29],[-35,24],[-34,49],[-33,-19],[-32,2],[-31,8],[-30,74],[-29,58],[-28,13],[-27,-8],[-26,45],[-25,-5],[-24,45],[-23,19],[-22,9],[-21,54],[-20,1],[-19,81],[-18,17],[-17,-10],[-16,7],[-15,86],[-14,-3],[-13,-3],[-12,45],[-11,93],[-10,84],[-9,20],[-8,3],[-7,81],[-6,52],[-5,67],[-4,18],[-3,40],[-2,42],[-1,49],[0,7],[1,104],[2,79],[3,37],[4,47],[5,69],[6,89],[7,110],[8,108],[9,19],[10,25],[11,48],[12,63],[13,94],[14,55],[15,119],[16,64],[17,122],[18,92],[19,37],[20,86],[21,84],[22,122],[23,37],[24,125],[25,99],[26,45],[27,63],[28,40],[29,97],[30,78],[31,102],[32,120],[33,91],[34,107],[35,62],[36,137],[37,55],[38,115],[39,46],[40,136],[41,78],[42,86],[43,106],[44,66],[45,141],[46,92],[47,132],[48,89],[49,61],[50,128],[51,155],[52,153],[53,78],[54,114],[55,84],[56,151],[57,123],[58,69],[59,91],[60,89],[61,73],[62,81],[63,139],[64,108],[65,165],[66,92],[67,117],[68,140],[69,109],[70,102],[71,171],[72,141],[73,117],[74,124],[75,171],[76,132],[77,142],[78,107],[79,132],[80,171],[81,104],[82,160],[83,128],[84,137],[85,176],[86,188],[87,178],[88,117],[89,115],[90,140],[91,165],[92,133],[93,114],[94,125],[95,135],[96,144],[97,114],[98,183],[99,157]]
) # 187
print test.eraseOverlapIntervals(
    [[-100,-98],[-99,-97],[-98,-96],[-97,-95],[-96,-94],[-95,-93],[-94,-92],[-93,-91],[-92,-90],[-91,-89],[-90,-88],[-89,-87],[-88,-86],[-87,-85],[-86,-84],[-85,-83],[-84,-82],[-83,-81],[-82,-80],[-81,-79],[-80,-78],[-79,-77],[-78,-76],[-77,-75],[-76,-74],[-75,-73],[-74,-72],[-73,-71],[-72,-70],[-71,-69],[-70,-68],[-69,-67],[-68,-66],[-67,-65],[-66,-64],[-65,-63],[-64,-62],[-63,-61],[-62,-60],[-61,-59],[-60,-58],[-59,-57],[-58,-56],[-57,-55],[-56,-54],[-55,-53],[-54,-52],[-53,-51],[-52,-50],[-51,-49],[-50,-48],[-49,-47],[-48,-46],[-47,-45],[-46,-44],[-45,-43],[-44,-42],[-43,-41],[-42,-40],[-41,-39],[-40,-38],[-39,-37],[-38,-36],[-37,-35],[-36,-34],[-35,-33],[-34,-32],[-33,-31],[-32,-30],[-31,-29],[-30,-28],[-29,-27],[-28,-26],[-27,-25],[-26,-24],[-25,-23],[-24,-22],[-23,-21],[-22,-20],[-21,-19],[-20,-18],[-19,-17],[-18,-16],[-17,-15],[-16,-14],[-15,-13],[-14,-12],[-13,-11],[-12,-10],[-11,-9],[-10,-8],[-9,-7],[-8,-6],[-7,-5],[-6,-4],[-5,-3],[-4,-2],[-3,-1],[-2,0],[-1,1],[0,2],[1,3],[2,4],[3,5],[4,6],[5,7],[6,8],[7,9],[8,10],[9,11],[10,12],[11,13],[12,14],[13,15],[14,16],[15,17],[16,18],[17,19],[18,20],[19,21],[20,22],[21,23],[22,24],[23,25],[24,26],[25,27],[26,28],[27,29],[28,30],[29,31],[30,32],[31,33],[32,34],[33,35],[34,36],[35,37],[36,38],[37,39],[38,40],[39,41],[40,42],[41,43],[42,44],[43,45],[44,46],[45,47],[46,48],[47,49],[48,50],[49,51],[50,52],[51,53],[52,54],[53,55],[54,56],[55,57],[56,58],[57,59],[58,60],[59,61],[60,62],[61,63],[62,64],[63,65],[64,66],[65,67],[66,68],[67,69],[68,70],[69,71],[70,72],[71,73],[72,74],[73,75],[74,76],[75,77],[76,78],[77,79],[78,80],[79,81],[80,82],[81,83],[82,84],[83,85],[84,86],[85,87],[86,88],[87,89],[88,90],[89,91],[90,92],[91,93],[92,94],[93,95],[94,96],[95,97],[96,98],[97,99],[98,100],[99,101]]
) # 100