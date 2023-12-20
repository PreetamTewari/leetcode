func twoSum(nums []int, target int) []int {
    dic := make(map[int]int)

    for index, number := range nums {
        if val, found := dic[target - number]; found {
            return []int{val, index}
        }
        dic[number] = index
    }
    return nil
}