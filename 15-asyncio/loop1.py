import asyncio

def estudiar():
    print ("leyendo")

def face():
    print ("likear")

loop = asyncio.get_event_loop()
#corre si nanda que hacer
loop.run_forever()

loop.call_soon(estudiar)
loop.call_later(2,face)
loop.call_later(5,estudiar)
#ejecuta todo lo registado
loop.run_forever()

#no hay nada registado
loop.run_forever()
loop.is_running()

loop.call_soon(estudiar)
loop.is_running()
#correr until_complete
loop.run_until_complete(asyncio.sleep(3))

