
def main():

    i = 1405046269503207469140791548403639533127416416214210694972085079171787580463776820425965898174272870486015739516125786182821637006600742140682552321645503743280670839819078749092730110549881891271317396450158021688253989767145578723458252769465545504142139663476747479225923933192421405464414574786272963741656223941750084051228611576708609346787101088759062724389874160693008783334605903142528824559223515203978707969795087506678894006628296743079886244349469131831225757926844843554897638786146036869572653204735650843186722732736888918789379054050122205253165705085538743651258400390580971043144644984654914856729
    print(hex(i))
    
    hex_string = "0xb214eea16966ad6a81477ce532a94f42e649434f1db9fefac6d05f930bf98dff145d803328acb98f371d033138daf5b623b8a3c77d491153a93dc17928b2cfa944768641a000a13da5d6e84aa777e250b3d275a9d5fdd237c73ceebfce849524c95951a94fd18773e6631cad21c7d6555cc3b00a324ed71e2ac23c075de3711572feac7f31835517ab442441cefa1dfa2a2a291f864b29a4e026e4ff5bd194ed6940f0ded6089a8754d31a33cc12e06d529ad29a2d424a439b0f5013f2f0e0ea8680b37532cd4029d29f10d22e27290bd5614b0d8ca3d9db66d5d893e015ee634b32eafba4ef149ad360f08fb13a6df5787eedf7816c68579102ed7b1e72719"[2:]
    print(hex_string)
    bytes_object = bytes.fromhex(hex_string)
    ascii_string = bytes_object.decode("ASCII")
    print(ascii_string)

    
if __name__=='__main__':
    main()
