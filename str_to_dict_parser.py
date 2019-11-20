test_str_one = """key1
{
    key11 value11;
}
key2
{
    key21 value21;
    key22 value22;
    key23 value23;
    key24 value24;
}
key3
{
    key31 value31;
    key32 value32;
    key33 value33;
    key34 value34;
    key35
    {
        key351 value351;
        key352 value352;
        key353
        {
            key3531 value3531;
        }
    }
}
"""
test_str_two = """key1
  {
      key11
      {
          key111 value111;
          key112
        {
            key1121 value1121;
        }
          key113 value113;
      };
      key12 value12;
      key13 value13;
      key14 value14;
      key15 value15;
      key16 
      {
         key161 value161;
      };
      key17 value17;
      key18 value18;
      key19 value19;
  };
  key2
  {
      key21 value21;
      key22 value22;
      key23 value23;
      key24 value24;
  };
  key3
  {
      key31 value31;
  };
"""
test_str_three = """key 1
    {
        key11 value11;
        key12 value12;
    }
    key 2
    {
        key21 value21;
        key22 value22;
    }
"""


def parse_one(test_data):
    result = {}
    stack = []
    current_name = ''

    for line in test_data.splitlines():
        line_splitted = line.strip().split()
        line_key = line_splitted[0]

        if '{' in line:
            continue

        if '}' in line:
            if len(stack) == 1:
                result.update(stack[0])
            else:
                key_to_append = list(stack[-2].keys())[0]
                stack[-2][key_to_append].update(stack[-1])
                current_name = key_to_append
            stack.pop()
            continue

        if not line.endswith(';'):
            current_name = line.strip()
            stack.append({current_name: {}})
            continue

        stack[-1][current_name][line_key] = line_splitted[1].strip(';')
    return result


def parse_two(config):
    result = {}
    stack = [result]
    lines = config.splitlines()
    block_name = ''

    for line in lines:
        line = line.strip()
        if '{' in line:
            current_block = stack[-1]
            new_block = current_block[block_name] = {}
            stack.append(new_block)
            continue

        if '}' in line:
            stack.pop()
            continue

        if ';' not in line:
            block_name = line
            continue

        key, value = line.strip(';').split(' ')
        current_block = stack[-1]
        current_block[key] = value

    return result