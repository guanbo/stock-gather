# Copyright 2021 guanbo
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
from . import Gather

MARKET='SS'

def main():
  _gather = Gather()
  _code = "60{code:04d}.SS"
  for c in range(0, 2000):
    _gather.pasre(_code.format(code=c))
  pass

if __name__ == "__main__":
  main()