# Magic numbers grabbed from https://en.wikipedia.org/wiki/List_of_file_signatures
import binascii
import os
listOf4HexValues = [
    {
        "hexLimit": 4,
        "magicNumber": "a1b2c3d4",
        "extension": ".pcap"

    },
    {
        "hexLimit": 4,
        "magicNumber": "d4c3b2a1",
        "extension": ".pcap"
    },
    {
        "hexLimit": 4,
        "magicNumber": "0a0d0d0a",
        "extension": ".pcapng"
    },
    {
        "hexLimit": 4,
        "magicNumber": "edabeedb",
        "extension": ".rpm"
    },
    {
        "hexLimit": 1,
        "magicNumber": "53514c69746520666f726d6174203300",
        "extension": ".sqlitedb .sqlite .db"
    },
    {
        "hexLimit": 4,
        "magicNumber": "53503031",
        "extension": ".bin"
    },
    {
        "hexLimit": 1,
        "magicNumber": "00",
        "extension": ".pic .pif .sea .ytr"
    },
    {
        "hexLimit": 24,
        "magicNumber": "000000000000000000000000000000000000000000000000",
        "extension": ".pdb"
    },
    {
        "hexLimit": 4,
        "magicNumber": "BEBAFECA",
        "extension": ".dba"
    },
    {
        "hexLimit": 4,
        "magicNumber": "00014244",
        "extension": ".dba"
    },
    {
        "hexLimit": 4,
        "magicNumber": "00014454",
        "extension": ".tda"
    },
    {
        "hexLimit": 4,
        "magicNumber": "54444624",
        "extension": ".tdf$"
    },
    {
        "hexLimit": 4,
        "magicNumber": "54444546",
        "extension": ".tdef"
    },
    {
        "hexLimit": 4,
        "magicNumber": "00010000",
        "extension": "none, Palm Desktop Data File (Access format)"
    },
    {
        "hexLimit": 4,
        "magicNumber": "00000100",
        "extension": ".ico"
    },
    {
        "hexLimit": 6,
        "magicNumber": "667479703367",
        "extension": ".3gp .3g2"
    },
    {
        "hexLimit": 2,
        "magicNumber": "1F9D",
        "extension": ".z .tar.z"
    },
    {
        "hexLimit": 2,
        "magicNumber": "1FA0",
        "extension": ".z .tar.z"
    },
    {
        "hexLimit": 12,
        "magicNumber": "4241434B4D494B454449534B",
        "extension": ".bac"
    },
    {
        "hexLimit": 3,
        "magicNumber": "425A68",
        "extension": ".bz2"
    },
    {
        "hexLimit": 6,
        "magicNumber": "474946383761",
        "extension": ".gif"
    },
    {
        "hexLimit": 6,
        "magicNumber": "474946383961",
        "extension": ".gif"
    },
    {
        "hexLimit": 4,
        "magicNumber": "49492A00",
        "extension": ".tif .tiff"
    },
    {
        "hexLimit": 4,
        "magicNumber": "4D4D002A",
        "extension": ".tif .tiff"
    },
    {
        "hexLimit": 8,
        "magicNumber": "49492A0010000000",
        "extension": ".cr2"
    },
    {
        "hexLimit": 4,
        "magicNumber": "802A5FD7",
        "extension": ".cin"
    },
    {
        "hexLimit": 4,
        "magicNumber": "524E4301",
        "extension": "none, Compressed file using Rob Northen Compression"
    },
    {
        "hexLimit": 4,
        "magicNumber": "524E4302",
        "extension": "none, Compressed file using Rob Northen Compression"
    },
    {
        "hexLimit": 4,
        "magicNumber": "53445058",
        "extension": ".dpx"
    },
    {
        "hexLimit": 4,
        "magicNumber": "58504453",
        "extension": ".dpx"
    },
    {
        "hexLimit": 4,
        "magicNumber": "762F3101",
        "extension": ".exr"
    },
    {
        "hexLimit": 4,
        "magicNumber": "425047FB",
        "extension": ".bpg"
    },
    {
        "hexLimit": 4,
        "magicNumber": "FFD8FFDB",
        "extension": ".jpg .jpeg"
    },
    {
        "hexLimit": 12,
        "magicNumber": "FFD8FFE000104A4649460001",
        "extension": ".jpg .jpeg"
    },
    {
        "hexLimit": 4,
        "magicNumber": "FFD8FFEE",
        "extension": ".jpg .jpeg"
    },
    {
        "hexLimit": 12,
        "magicNumber": "FFD8FFE1????457869660000",
        "extension": ".jpg .jpeg"
    },
    {
        "hexLimit": 12,
        "magicNumber": "464F524D????????494C424D",
        "extension": ".ilbm .lbm .ibm .iff"
    },
    {
        "hexLimit": 12,
        "magicNumber": "464F524D????????38535658",
        "extension": ".8svx .8sv .svx .snd .iff"
    },
    {
        "hexLimit": 12,
        "magicNumber": "464F524D????????4143424D",
        "extension": ".acbm .iff"
    },
    {
        "hexLimit": 12,
        "magicNumber": "464F524D????????414E424D",
        "extension": ".acbm .iff"
    },
    {
        "hexLimit": 12,
        "magicNumber": "464F524D????????414E494D",
        "extension": ".anim .iff"
    },
    {
        "hexLimit": 12,
        "magicNumber": "464F524D????????46415858",
        "extension": ".faxx .fax .iff"
    },
    {
        "hexLimit": 12,
        "magicNumber": "464F524D????????46545854",
        "extension": ".ftxt .iff"
    },
    {
        "hexLimit": 12,
        "magicNumber": "464F524D????????534D5553",
        "extension": ".smus .smu .mus .iff"
    },
    {
        "hexLimit": 12,
        "magicNumber": "464F524D????????434D5553",
        "extension": ".cmus .mus .iff"
    },
    {
        "hexLimit": 12,
        "magicNumber": "464F524D????????5955564E",
        "extension": ".yuvn .yuv .iff"
    },
    {
        "hexLimit": 12,
        "magicNumber": "464F524D????????46414E54",
        "extension": ".iff"
    },
    {
        "hexLimit": 12,
        "magicNumber": "464F524D????????41494646",
        "extension": ".aiff .aif .aifc .snd .iff"
    },
    {
        "hexLimit": 4,
        "magicNumber": "494E4458",
        "extension": ".idx"
    },
    {
        "hexLimit": 4,
        "magicNumber": "4C5A4950",
        "extension": ".lz"
    },
    {
        "hexLimit": 2,
        "magicNumber": "4D5A",
        "extension": ".exe .dll"
    },
    {
        "hexLimit": 4,
        "magicNumber": "504B0304",
        "extension": ".zip .aar .apk .docx .epub .ipa .jar .kmz .maff .odp .ods .odt .pk3 .pk4 .pptx .usdz .vsdx .xlsx .xpi"
    },
    {
        "hexLimit": 4,
        "magicNumber": "504B0506",
        "extension": ".zip .aar .apk .docx .epub .ipa .jar .kmz .maff .odp .ods .odt .pk3 .pk4 .pptx .usdz .vsdx .xlsx .xpi"
    },
    {
        "hexLimit": 4,
        "magicNumber": "504B0708",
        "extension": ".zip .aar .apk .docx .epub .ipa .jar .kmz .maff .odp .ods .odt .pk3 .pk4 .pptx .usdz .vsdx .xlsx .xpi"
    },
    {
        "hexLimit": 7,
        "magicNumber": "526172211A0700",
        "extension": ".rar"
    },
    {
        "hexLimit": 8,
        "magicNumber": "526172211A070100",
        "extension": ".rar"
    },
    {
        "hexLimit": 4,
        "magicNumber": "7F454C46",
        "extension": "none, Executable and Linkable Format"
    },
    {
        "hexLimit": 8,
        "magicNumber": "89504E470D0A1A0A",
        "extension": ".png"
    },
    {
        "hexLimit": 4,
        "magicNumber": "CAFEBABE",
        "extension": ".class"
    },
    {
        "hexLimit": 3,
        "magicNumber": "EFBBBF",
        "extension": "none, UTF-8 encoded Unicode byte order mark, commonly seen in text files."
    },
    {
        "hexLimit": 4,
        "magicNumber": "FEEDFACE",
        "extension": "none, Mach-O binary (32-bit)"
    },
    {
        "hexLimit": 4,
        "magicNumber": "FEEDFACF",
        "extension": "none, Mach-O binary (64-bit)"
    },
    {
        "hexLimit": 4,
        "magicNumber": "FEEDFEED",
        "extension": "none, JKS JavakeyStore"
    },
    {
        "hexLimit": 4,
        "magicNumber": "CEFAEDFE",
        "extension": "none, Mach-O binary (reverse byte ordering scheme, 32-bit)"
    },
    {
        "hexLimit": 4,
        "magicNumber": "CFFAEDFE",
        "extension": "none, Mach-O binary (reverse byte ordering scheme, 64-bit)"
    },
    {
        "hexLimit": 2,
        "magicNumber": "FFFE",
        "extension": "none, Byte-order mark for text file encoded in little-endian 16-bit Unicode Transfer Format"
    },
    {
        "hexLimit": 4,
        "magicNumber": "FFFE0000",
        "extension": "none, Byte-order mark for text file encoded in little-endian 32-bit Unicode Transfer Format"
    },
    {
        "hexLimit": 4,
        "magicNumber": "25215053",
        "extension": ".ps"
    },
    {
        "hexLimit": 5,
        "magicNumber": "255044462d",
        "extension": ".pdf"
    },
    {
        "hexLimit": 16,
        "magicNumber": "3026B2758E66CF11A6D900AA0062CE6C",
        "extension": ".asf .wma .wmv"
    },
    {
        "hexLimit": 8,
        "magicNumber": "2453444930303031",
        "extension": "none, System Deployment Image, a disk image format used by Microsoft"
    },
    {
        "hexLimit": 4,
        "magicNumber": "4F676753",
        "extension": ".ogg .oga .ogv"
    },
    {
        "hexLimit": 4,
        "magicNumber": "38425053",
        "extension": ".psd"
    },
    {
        "hexLimit": 12,
        "magicNumber": "52494646????????57415645",
        "extension": ".wav"
    },
    {
        "hexLimit": 12,
        "magicNumber": "52494646????????41564920",
        "extension": ".avi"
    },
    {
        "hexLimit": 2,
        "magicNumber": "FFFB",
        "extension": ".mp3"
    },
    {
        "hexLimit": 3,
        "magicNumber": "494433",
        "extension": ".mp3"
    },
    {
        "hexLimit": 2,
        "magicNumber": "424D",
        "extension": ".bmp .dib"
    },
    {
        "hexLimit": 5,
        "magicNumber": "4344303031",
        "extension:": ".iso"
    },
    {
        "hexLimit": 8,
        "magicNumber": "53494D504C452020",
        "extension:": ".fits"
    },
    {
        "hexLimit": 22,
        "magicNumber": "3D202020202020202020202020202020202020202054",
        "extension:": ".fits"
    },
    {
        "hexLimit": 4,
        "magicNumber": "664C6143",
        "extension:": ".flac"
    },

    {
        "hexLimit": 4,
        "magicNumber": "4D546864",
        "extension:": ".mid .midi"
    },
    {
        "hexLimit": 8,
        "magicNumber": "D0CF11E0A1B11AE1",
        "extension:": ".doc .xls .ppt .msg"
    },
    {
        "hexLimit": 8,
        "magicNumber": "6465780A30333500",
        "extension:": ".dex"
    },
    {
        "hexLimit": 3,
        "magicNumber": "4B444D",
        "extension:": ".vmdk"
    },
    {
        "hexLimit": 4,
        "magicNumber": "43723234",
        "extension:": ".crx"
    },
    {
        "hexLimit": 4,
        "magicNumber": "41474433",
        "extension:": ".fh8"
    },
    {
        "hexLimit": 22,
        "magicNumber": "05070000424F424F0507000000000000000000000001",
        "extension:": ".cwk"
    },
    {
        "hexLimit": 22,
        "magicNumber": "06 07 E1 00 42 4F 42 4F 06 07 E1 00 00 00 00 00 00 00 00 00 00 01",
        "extension:": ".cwk"
    },
    {
        "hexLimit": 6,
        "magicNumber": "455202000000",
        "extension:": ".toast"
    },
    {
        "hexLimit": 7,
        "magicNumber": "8B455202000000",
        "extension:": ".toast"
    },
    {
        "hexLimit": 7,
        "magicNumber": "78 01 73 0D 62 62 60",
        "extension:": ".dmg"
    },
    {
        "hexLimit": 4,
        "magicNumber": "78 61 72 21",
        "extension:": ".xar"
    },
    {
        "hexLimit": 8,
        "magicNumber": "504D4F43434D4F43",
        "extension:": ".dat"
    },
    {
        "hexLimit": 4,
        "magicNumber": "4E45531A",
        "extension:": ".nes"
    },
    {
        "hexLimit": 8,
        "magicNumber": "7573746172003030",
        "extension:": ".tar"
    },
    {
        "hexLimit": 8,
        "magicNumber": "7573746172202000",
        "extension:": ".tar"
    },
    {
        "hexLimit": 4,
        "magicNumber": "746F7833",
        "extension:": ".tox"
    },
    {
        "hexLimit": 4,
        "magicNumber": "4D4C5649",
        "extension:": ".MLV"
    },
    {
        "hexLimit": 8,
        "magicNumber": "44434D0150413330",
        "extension:": "none, Windows Update Binary Delta Compression"
    },
    {
        "hexLimit": 6,
        "magicNumber": "377ABCAF271C",
        "extension:": ".7z"
    },
    {
        "hexLimit": 2,
        "magicNumber": "1F8B",
        "extension:": ".gz .tar.gz"
    },
    {
        "hexLimit": 7,
        "magicNumber": "FD377A585A0000",
        "extension:": ".xz .tar.xz"
    },
    {
        "hexLimit": 4,
        "magicNumber": "04224D18",
        "extension:": ".lz4"
    },
    {
        "hexLimit": 4,
        "magicNumber": "4D534346",
        "extension:": ".cab"
    },
    {
        "hexLimit": 7,
        "magicNumber": "535A444488F02733",
        "extension:": ".ex?, ? can be replaced by anything"
    },
    {
        "hexLimit": 4,
        "magicNumber": "464C4946",
        "extension:": ".flif"
    },
    {
        "hexLimit": 4,
        "magicNumber": "1A45DFA3",
        "extension:": ".mkv .mka .mks .mk3d .webm"
    },
    {
        "hexLimit": 4,
        "magicNumber": "4D494C20",
        "extension:": ".stg"
    },
    {
        "hexLimit": 14,
        "magicNumber": "41542654464F524D????????444A56",
        "extension:": ".djvu .djv"
    },
    {
        "hexLimit": 2,
        "magicNumber": "3082",
        "extension:": ".der"
    },
    {
        "hexLimit": 4,
        "magicNumber": "4449434D",
        "extension:": ".dcm"
    },
    {
        "hexLimit": 4,
        "magicNumber": "774F4646",
        "extension:": ".woff"
    },
    {
        "hexLimit": 4,
        "magicNumber": "774F4632",
        "extension:": ".woff2"
    },
    {
        "hexLimit": 6,
        "magicNumber": "3c3f786d6c20",
        "extension:": ".XML"
    },
    {
        "hexLimit": 4,
        "magicNumber": "0061736d",
        "extension:": ".wasm"
    },
    {
        "hexLimit": 3,
        "magicNumber": "cf8401",
        "extension:": "3"
    },
    {
        "hexLimit": 3,
        "magicNumber": "435753",
        "extension:": ".swf"
    },
    {
        "hexLimit": 3,
        "magicNumber": "465753",
        "extension:": ".swf"
    },
    {
        "hexLimit": 7,
        "magicNumber": "213C617263683E",
        "extension:": ".deb"
    },
    {
        "hexLimit": 12,
        "magicNumber": "52494646????????57454250",
        "extension:": ".webp"
    },
    {
        "hexLimit": 4,
        "magicNumber": "27051956",
        "extension:": "none, U-Boot / uImage. Das U-Boot Universal Boot Loader."
    },
    {
        "hexLimit": 6,
        "magicNumber": "7B5C72746631",
        "extension:": ".rtf"
    },
    {
        "hexLimit": 4,
        "magicNumber": "54415045",
        "extension:": "none, Microsoft Tape Format"
    },
    {
        "hexLimit": 1,
        "magicNumber": "47",
        "extension:": ".ts .tsv .tsa"
    },
    {
        "hexLimit": 4,
        "magicNumber": "000001BA",
        "extension:": ".m2p .vob"
    },
    {
        "hexLimit": 4,
        "magicNumber": "000001BA",
        "extension:": ".mpg .mpeg"
    },
    {
        "hexLimit": 1,
        "magicNumber": "47",
        "extension:": ".mpg .mpeg"
    },
    {
        "hexLimit": 4,
        "magicNumber": "000001B3",
        "extension:": ".mpg .mpeg"
    },
    {
        "hexLimit": 2,
        "magicNumber": "7801",
        "extension:": ".zlib"
    },
    {
        "hexLimit": 2,
        "magicNumber": "789C",
        "extension:": ".zlib"
    },
    {
        "hexLimit": 2,
        "magicNumber": "78DA",
        "extension:": ".zlib"
    },
    {
        "hexLimit": 4,
        "magicNumber": "62767832",
        "extension:": ".lzfse"
    },
    {
        "hexLimit": 3,
        "magicNumber": "4F5243",
        "extension:": ".orc"
    },
    {
        "hexLimit": 4,
        "magicNumber": "4F626A01",
        "extension:": ".avro"
    },
    {
        "hexLimit": 4,
        "magicNumber": "53455136",
        "extension:": ".rc"
    },
    {
        "hexLimit": 4,
        "magicNumber": "65877856",
        "extension:": ".p25 .obt"
    },
    {
        "hexLimit": 4,
        "magicNumber": "5555aaaa",
        "extension:": ".pcv"
    },
    {
        "hexLimit": 3,
        "magicNumber": "785634",
        "extension:": ".pbt .pdt .pea .peb .pet .pgt .pict .pjt .pkt .pmt"
    },
    {
        "hexLimit": 4,
        "magicNumber": "50415231",
        "extension:": "none, Apache Parquet columnar file format"
    },
    {
        "hexLimit": 4,
        "magicNumber": "454D5832",
        "extension:": ".ez2"
    },
    {
        "hexLimit": 4,
        "magicNumber": "454D5533",
        "extension:": ".ez3 .iso"
    },
    {
        "hexLimit": 4,
        "magicNumber": "1B4C7561",
        "extension:": ".luac"
    },
    {
        "hexLimit": 16,
        "magicNumber": "62 6F 6F 6B 00 00 00 00 6D 61 72 6B 00 00 00 00",
        "extension:": ".alias"
    },
    {
        "hexLimit": 14,
        "magicNumber": "5B 5A 6F 6E 65 54 72 61 6E 73 66 65 72 5D",
        "extension:": ".identifier"
    },
    {
        "hexLimit": 8,
        "magicNumber": "52 65 63 65 69 76 65 64",
        "extension:": ".eml"
    },
    {
        "hexLimit": 12,
        "magicNumber": "20020162A01EAB0702000000",
        "extension:": ".tde"
    },
    {
        "hexLimit": 15,
        "magicNumber": "3748030200000000583530394B4559",
        "extension:": ".kdb"
    },
    {
        "hexLimit": 4,
        "magicNumber": "28B52FFD",
        "extension:": ".zst"
    },
    {
        "hexLimit": 3,
        "magicNumber": "3A290A",
        "extension:": ".sml"
    }
]

os.system("clear")
print("Welcome to CheckFiler! \n")
testFile = raw_input("Enter the name of the file: ")
print("What do you want to do today?\n")
print("1. Chech the extension of the file\n2. Check if the file is corrupted or not")
option = input("Input only the number of the option: ")
os.system("clear")
if option == 1:
    with open(testFile, 'rb') as f:
        content = f.read()
    os.system("clear")
    print("Printing the hex values of the script")
    # print(binascii.hexlify(content))

    for dictGrabber in listOf4HexValues:
        limitGrab = dictGrabber.get("hexLimit")
        hexGrab = dictGrabber.get("magicNumber").lower()
        grabbingLimit = 0
        grabbedHex = ""
        # import pdb
        # pdb.set_trace()
        while grabbingLimit < limitGrab:
            grabbedHex = grabbedHex + binascii.hexlify(content[grabbingLimit])
            grabbingLimit = grabbingLimit + 1
        if grabbedHex == hexGrab:
            print("Found a match")
            kindOfFile = dictGrabber.get("extension")
            print(kindOfFile)
        else:
            continue
elif option == 2:
    print("Checking if the file is corrupted or not..")
else:
    print("That was not a valid option")
