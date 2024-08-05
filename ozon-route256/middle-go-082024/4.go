package main

import (
	"bufio"
	"fmt"
	"os"
)

func longestSubarrayWithTwoDistinct(nums []int) int {
	n := len(nums)
	if n == 0 {
		return 0
	}

	left := 0
	right := 0
	maxLen := 0
	count := make(map[int]int)

	for right < n {
		count[nums[right]]++
		right++

		for len(count) > 2 {
			count[nums[left]]--
			if count[nums[left]] == 0 {
				delete(count, nums[left])
			}
			left++
		}

		if currentLen := right - left; currentLen > maxLen {
			maxLen = currentLen
		}
	}

	return maxLen
}

func packAddrs(n []int) []interface{} {
	p := make([]interface{}, len(n))
	for i := range n {
		p[i] = &n[i]
	}
	return p
}

func main() {
	var in *bufio.Reader
	var out *bufio.Writer
	in = bufio.NewReader(os.Stdin)
	out = bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var reader_count int
	var arr_len int

	fmt.Fscan(in, &reader_count)
	for ; reader_count > 0; reader_count-- {
		fmt.Fscan(in, &arr_len)
		nodes := make([]int, arr_len)

		fmt.Fscan(in, packAddrs(nodes)...)
		var res = longestSubarrayWithTwoDistinct(nodes)
		fmt.Fprintf(out, "%d\n", res)
	}
}
