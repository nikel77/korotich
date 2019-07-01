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


def list_then_dict(input):
    key_list = []
    value_list = []
    while input:
        if input[0] != '}' and ";" not in input[0] and input[0] != '{':
            key_list.append(input[0])
            input.remove(input[0])
        elif input[0] != '}' and ";" in input[0]:
            value_list.append(input[0].strip(';'))
            input.remove(input[0])
        elif input[0] == '{':
            input.remove(input[0])
            value_list.append(list_then_dict(input))
        else:
            input.remove(input[0])
            break
    return {key: value for key, value in zip(key_list, value_list)}


def str_then_dict(input):
    input = input.replace('};', '}')
    input = input.split()
    return list_then_dict(input)


print(str_then_dict(test_str_one))
print(str_then_dict(test_str_two))
