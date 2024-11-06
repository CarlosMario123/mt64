from mt.textBin import TuringMachineToBinary
from mt.group24bits import TuringMachineGroup24Bits
from mt.divideGroupBites import TuringMachineDivide6Bits
from mt.map64 import TuringMachineMapBase64
def generateConvert(text):
    mt_bi = TuringMachineToBinary(text)
    result = mt_bi.run()
    mt_24bits = TuringMachineGroup24Bits(result)
    result = mt_24bits.run()
    mt_divide_6_bits = TuringMachineDivide6Bits(result)
    result = mt_divide_6_bits.run()
    mt_map64 = TuringMachineMapBase64(result)
    result = mt_map64.run()
    return result
     
    
    