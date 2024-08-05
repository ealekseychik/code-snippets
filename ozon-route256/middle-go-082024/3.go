/*
	Рекомендуется использовать быстрый (буферизованный) ввод и вывод

var in *bufio.Reader
var out *bufio.Writer
in = bufio.NewReader(os.Stdin)
out = bufio.NewWriter(os.Stdout)
defer out.Flush()

var a, b int
fmt.Fscan(in, &a, &b)
fmt.Fprint(out, a + b)
*/
package main

import (
	"bufio"
	"fmt"
	"os"
)

func findRoot(nodes []int) int {
	// Create a map to keep track of nodes and their sub-nodes count
	nodeToSubNodesCount := make(map[int]int)

	// Create a map to keep track of all nodes and their parent relationship
	nodeToParent := make(map[int]int)

	// Parse the input array
	i := 0
	for i < len(nodes) {
		node := nodes[i]
		subNodeCount := nodes[i+1]
		nodeToSubNodesCount[node] = subNodeCount
		for j := 0; j < subNodeCount; j++ {
			subNode := nodes[i+2+j]
			nodeToParent[subNode] = node
		}
		i += 2 + subNodeCount
	}

	// The root node is the one that does not have a parent
	for node := range nodeToSubNodesCount {
		if _, exists := nodeToParent[node]; !exists {
			return node
		}
	}

	// If no root is found, return -1 (indicating an error)
	return -1
}

func packAddrs(n []int, out *bufio.Writer) []interface{} {
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

		fmt.Fscan(in, packAddrs(nodes, out)...)
		var res = findRoot(nodes)
		fmt.Fprintf(out, "%d\n", res)
	}
}
