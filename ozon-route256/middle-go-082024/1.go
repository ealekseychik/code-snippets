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
	var out *bufio.Writer
	out = bufio.NewWriter(os.Stdout)
	defer out.Flush()

	fmt.Fprint(out, "OK")
}
