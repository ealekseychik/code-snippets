// Accepted with TL (20/30)

package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

func minTransportations(vehicles, capacity int, boxes []int) int {
	// Sort boxes in descending order
	sort.Sort(sort.Reverse(sort.IntSlice(boxes)))

	trips := 0
	for len(boxes) > 0 {
		// Initialize the remaining capacity for each vehicle for this trip
		remainingCapacity := make([]int, vehicles)
		for i := range remainingCapacity {
			remainingCapacity[i] = capacity
		}

		// Try to pack boxes into vehicles for this trip
		i := 0
		for i < len(boxes) {
			placed := false
			for j := range remainingCapacity {
				if remainingCapacity[j] >= boxes[i] {
					remainingCapacity[j] -= boxes[i]
					// Remove the box from the list
					boxes = append(boxes[:i], boxes[i+1:]...)
					placed = true
					break
				}
			}
			if !placed {
				i++
			}
		}

		trips++
	}

	return trips
}

func packAddrs(n []int) []interface{} {
	p := make([]interface{}, len(n))
	for i := range n {
		p[i] = &n[i]
	}
	return p
}

func packPower(n []int) []int {
	p := make([]int, len(n))  // Create a new slice to hold the results
	for i, value := range n { // Iterate over the elements of the input slice
		p[i] = 1 << value // Compute 2^value and store it in the result slice
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
	var num_cars,
		car_weight int
	var num_boxes int

	fmt.Fscan(in, &reader_count)
	for ; reader_count > 0; reader_count-- {
		fmt.Fscan(in, &num_cars, &car_weight)
		fmt.Fscan(in, &num_boxes)

		boxes_weight := make([]int, num_boxes)

		fmt.Fscan(in, packAddrs(boxes_weight)...)
		new_boxes_weight := packPower(boxes_weight)
		var res = minTransportations(num_cars, car_weight, new_boxes_weight)
		fmt.Fprintf(out, "%d\n", res)
	}
}
