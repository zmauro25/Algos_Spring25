'''Lorenzo, Jonathan, Erasmo, Konstantinos and Clover like to take long walks
and discuss problems for next week. On one of those days, they were looking at
downtown Chicago from the Promontory Point in Hyde Park and were wondering how
an algorithm would construct a rendering of the view given information about the
location and height of the buildings. Thankfully, the student in Theory of
Algorithms can definitely help.

Assume every building is given as three integers $(left_i, width_i, height_i)$,
where $left_i$ indicates the distance at which building $i$ starts,  $width_i$
is the building's width and $height_i$ is its height. You need to return a list
of intervals $(x_j, h_j)$, denoting the distance at which $x_j$ which correspond
with where a height change starts and what the new height is.

{\\bf Input:}
The first line contains a single integer $N$, the number of buildings. $N$ lines
follow. Each line has three integers; where the building starts on the $x$-axis,
its width and its height. DO NOT ASSUME THEY ARE ORDERED.

{\\bf Output:}
You need to print out the height segments. In every line there should be two
integers. The first one designates where the segment startsand the second is the
height.'''

def add_p(arr, x_coor, y_coor):
  # takes in the result skyline array and a point (x_coor, y_coor) to add to the 
  # result! 

  prev_X = arr[-1][0]
  prev_Y = arr[-1][1]
  if arr and prev_X == x_coor: 
    arr[-1][1] = y_coor
    return arr
  if arr and prev_Y == y_coor:
    return arr 
  arr.append([x_coor, y_coor])

  return arr 

def merge_shadows(l, r):
  # Takes in two shadows l and r
  # l and r are a list of the x and y coordinates 
  merged = []
  l_len = len(l)
  r_len = len(r)
  i, j = 0
  l_Y, r_Y = 0

  while i < l_len and j < r_len:
    curr_l_Y = left[i][1]
    curr_r_Y = right[j][1]

    curr_l_X = left[i][0]
    curr_r_X = right[j][0]
    
    # Start with the smaller of the left or right x-coord
    if curr_l_X < curr_r_X: 
      l_height = curr_l_height 
      new_height = max(curr_l_Y, r_Y)
      add_p(merged, curr_l_X, new_height)
      i += 1 
    else:
      r_height = curr_r_height
      new_height = max(curr_r_Y, l_Y)
      add_p(merged, curr_r_X, new_height)
      j += 1 
    
  # Add the left over points from the left:  
  while i < l_len: 
    add_p(merged, left[i][0], left[i][1])
    i += 1 
  
  # Add the left over points from the right:
  while j < r_len:
    add_p(merged, right[j][0], left[j][1])
    j += 1

  return merged
      


def solve(N, rectangles):
    # BASE CASE: When there are no rectangles left, return empty list 
    if N == 0:
      return []

    # BASE CASE: When there is one rectangle left, return shadow
    if N == 1: 
      x1 = rectangles[0]
      y1 = rectangles[2]
      x2 = rectangles[0] + rectangles[1]
      y2 = 0
      return [[x1, y1],[x2,y2]]
    
    # RECURSION: 
    center = N // 2
    left = rectangles[center:]
    right = rectangles[:center]
    return merge_shadows(solve(len(left), left), solve(len(right), right))

def print_solution(intervals):
    for x, h in intervals:
        print(x, h)


def main():
    N = int(input)
    rectangles = [[int(i) for i in input().split()] for _ in range(N)]
    intervals = solve(N, rectangles)
    print_solution(intervals)


if __name__ == '__main__':
    main()