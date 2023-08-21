import pprint
import google.generativeai as palm

# PaLM_KEY='AIzaSyDrALuM4Xiq8E7OaKnjRRPqcwLYLQvCIMc'
# PaLM_KEY='AIzaSyBfaCJDTjo0bTKLrSF2nBQoq7zWVPnBB7k'
PaLM_KEY='AIzaSyAu6SlHQt8VTvBxx5nSYYmsBLVfvTouyeY'
palm.configure(api_key=PaLM_KEY)

# models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
# models = [m for m in palm.list_models() ]
# model = models[0].name
# print(model)

# model_list =[_ for _ in palm.list_models()]
# for model in model_list:
#     print(model.name)

model_id= 'models/text-bison-001'
prompt='''
    write a marckiting proposal to sell an ice cream product. limit the proposal to 50 words
'''
completion = palm.generate_text(
    model = model_id,
    prompt=prompt,
    temperature = 0,
    max_output_tokens=800,#The Max Lenth of the Response
    # candidate_count=1
    candidate_count=2
)
# print(completion)
# completion.result
outputs=[output['output'] for output in completion.candidates]
for output in outputs:
    print(output)
    print('-'*50)