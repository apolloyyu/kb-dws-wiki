// Build-time source projector. Standard library only; no business code runs.
package main

import (
 "encoding/json"
 "fmt"
 "go/ast"
 "go/parser"
 "go/token"
 "os"
)

type Envelope struct {
 Line int `json:"line"`
 EndLine int `json:"end_line"`
 Source string `json:"source"`
}
type Result struct {
 Functions []Envelope `json:"functions"`
 Error string `json:"error,omitempty"`
}
func main() {
 var input map[string]string
 if err := json.NewDecoder(os.Stdin).Decode(&input); err != nil { fmt.Fprintln(os.Stderr,err); os.Exit(2) }
 result := make(map[string]Result)
 for path, source := range input {
  fset := token.NewFileSet()
  file, err := parser.ParseFile(fset,path,source,parser.ParseComments)
  if err != nil { result[path] = Result{Error:err.Error()}; continue }
  rows := []Envelope{}
  for _, declaration := range file.Decls {
   fn, ok := declaration.(*ast.FuncDecl)
   if !ok || fn.Body == nil { continue }
   start, end := fset.Position(fn.Pos()), fset.Position(fn.End())
   if start.Offset < 0 || end.Offset > len(source) || end.Offset <= start.Offset { continue }
   rows = append(rows, Envelope{Line:start.Line,EndLine:end.Line,Source:source[start.Offset:end.Offset]})
  }
  result[path] = Result{Functions:rows}
 }
 if err := json.NewEncoder(os.Stdout).Encode(result); err != nil { fmt.Fprintln(os.Stderr,err); os.Exit(2) }
}
