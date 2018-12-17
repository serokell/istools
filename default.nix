with import <nixpkgs> {};
with python3Packages;

buildPythonApplication {
  name = "istools";
  src = lib.cleanSource ./.;
}
