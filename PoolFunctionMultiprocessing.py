#pool function in multiprocessing
import multiprocessing
import time
def square(x):
    return x*x
# if __name__=="__main__":
#     pool=multiprocessing.Pool()
#     pool=multiprocessing.Pool(processes=4)
#     inputs=[0,1,2,3,4]
#     outputs=pool.map(square,inputs)
#     print("inputs:{}".format(inputs))
#     print("outputs: {}".format(outputs))
# 
# pool.map_async()
# if __name__=="__main__":
#     pool=multiprocessing.Pool()
#     inputs=[0,1,2,3,4]
#     outputs_async=pool.map_async(square,inputs)
#     outputs=outputs_async.get()
#     print("output:{}".format(outputs))
if __name__=="__main__":
    pool=multiprocessing.Pool()
    result_async=[pool.apply_async(square,args=(i, ))for i in range(10)]
    results=[r.get() for r in result_async]
    print("output:{}".format(results))