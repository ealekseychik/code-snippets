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

func main() {
	var in *bufio.Reader
	var out *bufio.Writer
	in = bufio.NewReader(os.Stdin)
	out = bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var reader_count int
	var lot_count, lot_perc int
	var price int
	var totes float64

	fmt.Fscan(in, &reader_count)
	for ; reader_count > 0; reader_count-- {
		fmt.Fscan(in, &lot_count, &lot_perc)
		for ; lot_count > 0; lot_count-- {
			fmt.Fscan(in, &price)
			//fmt.Printf("%d %d %d || %d\n", totes, price, lot_perc, lot_count)
			totes = totes + float64((price*lot_perc)%100)/100
		}
		//fmt.Printf("!!%d %.2f\n", lot_count, totes)
		fmt.Fprintf(out, "%.2f\n", totes)
		totes = 0
	}
}
