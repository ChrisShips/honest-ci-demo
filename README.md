

# honest-ci demo

A small shop's pricing code, in integer cents, with six pytest tests.

`main` has honest-ci installed the way `honest-ci init --github` writes it.
Each branch off it is one change a coding agent might hand in, and the pull
request from it into `main` shows what honest-ci makes of that change.
`before-honest-ci` is the shop before honest-ci and `install-honest-ci` the
change that installed it, so that installing can be tried as a pull request
too.

Built by `examples/python-agent-demo/github-demo.sh` in
[honest-ci](https://github.com/ChrisShips/honest-ci), whose `GITHUB.md` next to
that script says what each pull request should show.
