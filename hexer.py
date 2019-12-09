# List of Magic numbers grabbed from https://en.wikipedia.org/wiki/List_of_file_signatures

import binascii
import os
listOf4HexValues = [
    {
        "variation": 0,
        "hexLimit": 4,
        "magicNumber": "a1b2c3d4",
        "extension": ".pcap"

    },
    {
        "variation": 0,
        "hexLimit": 4,
        "magicNumber": "d4c3b2a1",
        "extension": ".pcap"
    },
    {
        "variation": 0,
        "hexLimit": 4,
        "magicNumber": "0a0d0d0a",
        "extension": ".pcapng"
    },
    {
        "variation": 0,
        "hexLimit": 4,
        "magicNumber": "edabeedb",
        "extension": ".rpm"
    },
    {
        "variation": 0,
        "hexLimit": 1,
        "magicNumber": "53514c69746520666f726d6174203300",
        "extension": ".sqlitedb .sqlite .db"
    },
    {
        "variation": 0,
        "hexLimit": 4,
        "magicNumber": "53503031",
        "extension": ".bin"
    },
    {
        "variation": 0,
        "hexLimit": 1,
        "magicNumber": "00",
        "extension": ".pic .pif .sea .ytr"
    },
    {
        "variation": 0,
        "hexLimit": 24,
        "magicNumber": "000000000000000000000000000000000000000000000000",
        "extension": ".pdb"
    },
    {
        "variation": 0,
        "hexLimit": 4,
        "magicNumber": "BEBAFECA",
        "extension": ".dba"
    },
    {
        "variation": 0,
        "hexLimit": 4,
        "magicNumber": "00014244",
        "extension": ".dba"
    },
    {
        "variation": 0,
        "hexLimit": 4,
        "magicNumber": "00014454",
        "extension": ".tda"
    },
    {
        "variation": 0,
        "hexLimit": 4,
        "magicNumber": "54444624",
        "extension": ".tdf$"
    },
    {
        "variation": 0,
        "hexLimit": 4,
        "magicNumber": "54444546",
        "extension": ".tdef"
    },
    {
        "variation": 0,
        "hexLimit": 4,
        "magicNumber": "00010000",
        "extension": "none, Palm Desktop Data File (Access format)"
    },
    {
        "variation": 0,
        "hexLimit": 4,
        "magicNumber": "00000100",
        "extension": ".ico"
    },
    {
        "variation": 0,
        "hexLimit": 6,
        "magicNumber": "667479703367",
        "extension": ".3gp .3g2"
    },
    {
        "variation": 0,
        "hexLimit": 2,
        "magicNumber": "1F9D",
        "extension": ".z .tar.z"
    },
    {
        "variation": 0,
        "hexLimit": 2,
        "magicNumber": "1FA0",
        "extension": ".z .tar.z"
    },
    {
        "variation": 0,
        "hexLimit": 12,
        "magicNumber": "4241434B4D494B454449534B",
        "extension": ".bac"
    },
    {
        "variation": 0,
        "hexLimit": 3,
        "magicNumber": "425A68",
        "extension": ".bz2"
    },
    {
        "variation": 0,
        "hexLimit": 6,
        "magicNumber": "474946383761",
        "extension": ".gif"
    },
    {
        "variation": 0,
        "hexLimit": 6,
        "magicNumber": "474946383961",
        "extension": ".gif"
    },
    {
        "variation": 0,
        "hexLimit": 4,
        "magicNumber": "49492A00",
        "extension": ".tif .tiff"
    },
    {
        "variation": 0,
        "hexLimit": 4,
        "magicNumber": "4D4D002A",
        "extension": ".tif .tiff"
    },
    {
        "variation": 0,
        "hexLimit": 8,
        "magicNumber": "49492A0010000000",
        "extension": ".cr2"
    },
    {
        "variation": 0,
        "hexLimit": 4,
        "magicNumber": "802A5FD7",
        "extension": ".cin"
    },
    {
        "variation": 0,
        "hexLimit": 4,
        "magicNumber": "524E4301",
        "extension": "none, Compressed file using Rob Northen Compression"
    },
    {
        "variation": 0,
        "hexLimit": 4,
        "magicNumber": "524E4302",
        "extension": "none, Compressed file using Rob Northen Compression"
    },
    {
        "variation": 0,
        "hexLimit": 4,
        "magicNumber": "53445058",
        "extension": ".dpx"
    },
    {
        "variation": 0,
        "hexLimit": 4,
        "magicNumber": "58504453",
        "extension": ".dpx"
    },
    {
        "variation": 0,
        "hexLimit": 4,
        "magicNumber": "762F3101",
        "extension": ".exr"
    },
    {
        "variation": 0,
        "hexLimit": 4,
        "magicNumber": "425047FB",
        "extension": ".bpg"
    },
    {
        "variation": 0,
        "hexLimit": 4,
        "magicNumber": "FFD8FFDB",
        "extension": ".jpg .jpeg"
    },
    {
        "variation": 0,
        "hexLimit": 12,
        "magicNumber": "FFD8FFE000104A4649460001",
        "extension": ".jpg .jpeg"
    },
    {
        "variation": 0,
        "hexLimit": 4,
        "magicNumber": "FFD8FFEE",
        "extension": ".jpg .jpeg"
    },
    {
        "variation": 1,
        "hexLimit": 12,
        "magicNumber": "FFD8FFE1????457869660000",
        "extension": ".jpg .jpeg"
    },
    {
        "variation": 1,
        "hexLimit": 12,
        "magicNumber": "464F524D????????494C424D",
        "extension": ".ilbm .lbm .ibm .iff"
    },
    {
        "variation": 1,
        "hexLimit": 12,
        "magicNumber": "464F524D????????38535658",
        "extension": ".8svx .8sv .svx .snd .iff"
    },
    {
        "variation": 1,
        "hexLimit": 12,
        "magicNumber": "464F524D????????4143424D",
        "extension": ".acbm .iff"
    },
    {
        "variation": 1,
        "hexLimit": 12,
        "magicNumber": "464F524D????????414E424D",
        "extension": ".acbm .iff"
    },
    {
        "variation": 1,
        "hexLimit": 12,
        "magicNumber": "464F524D????????414E494D",
        "extension": ".anim .iff"
    },
    {
        "variation": 1,
        "hexLimit": 12,
        "magicNumber": "464F524D????????46415858",
        "extension": ".faxx .fax .iff"
    },
    {
        "variation": 1,
        "hexLimit": 12,
        "magicNumber": "464F524D????????46545854",
        "extension": ".ftxt .iff"
    },
    {
        "variation": 1,
        "hexLimit": 12,
        "magicNumber": "464F524D????????534D5553",
        "extension": ".smus .smu .mus .iff"
    },
    {
        "variation": 1,
        "hexLimit": 12,
        "magicNumber": "464F524D????????434D5553",
        "extension": ".cmus .mus .iff"
    },
    {
        "variation": 1,
        "hexLimit": 12,
        "magicNumber": "464F524D????????5955564E",
        "extension": ".yuvn .yuv .iff"
    },
    {
        "variation": 1,
        "hexLimit": 12,
        "magicNumber": "464F524D????????46414E54",
        "extension": ".iff"
    },
    {
        "variation": 1,
        "hexLimit": 12,
        "magicNumber": "464F524D????????41494646",
        "extension": ".aiff .aif .aifc .snd .iff"
    },
    {
        "variation": 0,
        "hexLimit": 4,
        "magicNumber": "494E4458",
        "extension": ".idx"
    },
    {
        "variation": 0,
        "hexLimit": 4,
        "magicNumber": "4C5A4950",
        "extension": ".lz"
    },
    {
        "variation": 0,
        "hexLimit": 2,
        "magicNumber": "4D5A",
        "extension": ".exe .dll"
    },
    {
        "variation": 0,
        "hexLimit": 4,
        "magicNumber": "504B0304",
        "extension": ".zip .aar .apk .docx .epub .ipa .jar .kmz .maff .odp .ods .odt .pk3 .pk4 .pptx .usdz .vsdx .xlsx .xpi"
    },
    {
        "variation": 0,
        "hexLimit": 7,
        "magicNumber": "526172211A0700",
        "extension": ".rar"
    },
    {
        "variation": 0,
        "hexLimit": 8,
        "magicNumber": "526172211A070100",
        "extension": ".rar"
    },
    {
        "variation": 0,
        "hexLimit": 4,
        "magicNumber": "7F454C46",
        "extension": "none, Executable and Linkable Format"
    },
    {
        "variation": 0,
        "hexLimit": 8,
        "magicNumber": "89504E470D0A1A0A",
        "extension": ".png"
    },
    {
        "variation": 0,
        "hexLimit": 4,
        "magicNumber": "CAFEBABE",
        "extension": ".class"
    },
    {
        "variation": 0,
        "hexLimit": 3,
        "magicNumber": "EFBBBF",
        "extension": "none, UTF-8 encoded Unicode byte order mark, commonly seen in text files."
    },
    {
        "variation": 0,
        "hexLimit": 4,
        "magicNumber": "FEEDFACE",
        "extension": "none, Mach-O binary (32-bit)"
    },
    {
        "variation": 0,
        "hexLimit": 4,
        "magicNumber": "FEEDFACF",
        "extension": "none, Mach-O binary (64-bit)"
    },
    {
        "variation": 0,
        "hexLimit": 4,
        "magicNumber": "FEEDFEED",
        "extension": "none, JKS JavakeyStore"
    },
    {
        "variation": 0,
        "hexLimit": 4,
        "magicNumber": "CEFAEDFE",
        "extension": "none, Mach-O binary (reverse byte ordering scheme, 32-bit)"
    },
    {
        "variation": 0,
        "hexLimit": 4,
        "magicNumber": "CFFAEDFE",
        "extension": "none, Mach-O binary (reverse byte ordering scheme, 64-bit)"
    },
    {
        "variation": 0,
        "hexLimit": 2,
        "magicNumber": "FFFE",
        "extension": "none, Byte-order mark for text file encoded in little-endian 16-bit Unicode Transfer Format"
    },
    {
        "variation": 0,
        "hexLimit": 4,
        "magicNumber": "FFFE0000",
        "extension": "none, Byte-order mark for text file encoded in little-endian 32-bit Unicode Transfer Format"
    },
    {
        "variation": 0,
        "hexLimit": 4,
        "magicNumber": "25215053",
        "extension": ".ps"
    },
    {
        "variation": 0,
        "hexLimit": 5,
        "magicNumber": "255044462d",
        "extension": ".pdf"
    },
    {
        "variation": 0,
        "hexLimit": 16,
        "magicNumber": "3026B2758E66CF11A6D900AA0062CE6C",
        "extension": ".asf .wma .wmv"
    },
    {
        "variation": 0,
        "hexLimit": 8,
        "magicNumber": "2453444930303031",
        "extension": "none, System Deployment Image, a disk image format used by Microsoft"
    },
    {
        "variation": 0,
        "hexLimit": 4,
        "magicNumber": "4F676753",
        "extension": ".ogg .oga .ogv"
    },
    {
        "variation": 0,
        "hexLimit": 4,
        "magicNumber": "38425053",
        "extension": ".psd"
    },
    {
        "variation": 1,
        "hexLimit": 12,
        "magicNumber": "52494646????????57415645",
        "extension": ".wav"
    },
    {
        "variation": 1,
        "hexLimit": 12,
        "magicNumber": "52494646????????41564920",
        "extension": ".avi"
    },
    {
        "variation": 0,
        "hexLimit": 2,
        "magicNumber": "FFFB",
        "extension": ".mp3"
    },
    {
        "variation": 0,
        "hexLimit": 3,
        "magicNumber": "494433",
        "extension": ".mp3"
    },
    {
        "variation": 0,
        "hexLimit": 2,
        "magicNumber": "424D",
        "extension": ".bmp .dib"
    },
    {
        "variation": 0,
        "hexLimit": 5,
        "magicNumber": "4344303031",
        "extension": ".iso"
    },
    {
        "variation": 0,
        "hexLimit": 8,
        "magicNumber": "53494D504C452020",
        "extension": ".fits"
    },
    {
        "variation": 0,
        "hexLimit": 22,
        "magicNumber": "3D202020202020202020202020202020202020202054",
        "extension": ".fits"
    },
    {
        "variation": 0,
        "hexLimit": 4,
        "magicNumber": "664C6143",
        "extension": ".flac"
    },

    {
        "variation": 0,
        "hexLimit": 4,
        "magicNumber": "4D546864",
        "extension": ".mid .midi"
    },
    {
        "variation": 0,
        "hexLimit": 8,
        "magicNumber": "D0CF11E0A1B11AE1",
        "extension": ".doc .xls .ppt .msg"
    },
    {
        "variation": 0,
        "hexLimit": 8,
        "magicNumber": "6465780A30333500",
        "extension": ".dex"
    },
    {
        "variation": 0,
        "hexLimit": 3,
        "magicNumber": "4B444D",
        "extension": ".vmdk"
    },
    {
        "variation": 0,
        "hexLimit": 4,
        "magicNumber": "43723234",
        "extension": ".crx"
    },
    {
        "variation": 0,
        "hexLimit": 4,
        "magicNumber": "41474433",
        "extension": ".fh8"
    },
    {
        "variation": 0,
        "hexLimit": 22,
        "magicNumber": "05070000424F424F0507000000000000000000000001",
        "extension": ".cwk"
    },
    {
        "variation": 0,
        "hexLimit": 22,
        "magicNumber": "0607E100424F424F0607E10000000000000000000001",
        "extension": ".cwk"
    },
    {
        "variation": 0,
        "hexLimit": 6,
        "magicNumber": "455202000000",
        "extension": ".toast"
    },
    {
        "variation": 0,
        "hexLimit": 7,
        "magicNumber": "8B455202000000",
        "extension": ".toast"
    },
    {
        "variation": 0,
        "hexLimit": 7,
        "magicNumber": "78 01 73 0D 62 62 60",
        "extension": ".dmg"
    },
    {
        "variation": 0,
        "hexLimit": 4,
        "magicNumber": "78 61 72 21",
        "extension": ".xar"
    },
    {
        "variation": 0,
        "hexLimit": 8,
        "magicNumber": "504D4F43434D4F43",
        "extension": ".dat"
    },
    {
        "variation": 0,
        "hexLimit": 4,
        "magicNumber": "4E45531A",
        "extension": ".nes"
    },
    {
        "variation": 0,
        "hexLimit": 8,
        "magicNumber": "7573746172003030",
        "extension": ".tar"
    },
    {
        "variation": 0,
        "hexLimit": 8,
        "magicNumber": "7573746172202000",
        "extension": ".tar"
    },
    {
        "variation": 0,
        "hexLimit": 4,
        "magicNumber": "746F7833",
        "extension": ".tox"
    },
    {
        "variation": 0,
        "hexLimit": 4,
        "magicNumber": "4D4C5649",
        "extension": ".MLV"
    },
    {
        "variation": 0,
        "hexLimit": 8,
        "magicNumber": "44434D0150413330",
        "extension": "none, Windows Update Binary Delta Compression"
    },
    {
        "variation": 0,
        "hexLimit": 6,
        "magicNumber": "377ABCAF271C",
        "extension": ".7z"
    },
    {
        "variation": 0,
        "hexLimit": 2,
        "magicNumber": "1F8B",
        "extension": ".gz .tar.gz"
    },
    {
        "variation": 0,
        "hexLimit": 7,
        "magicNumber": "FD377A585A0000",
        "extension": ".xz .tar.xz"
    },
    {
        "variation": 0,
        "hexLimit": 4,
        "magicNumber": "04224D18",
        "extension": ".lz4"
    },
    {
        "variation": 0,
        "hexLimit": 4,
        "magicNumber": "4D534346",
        "extension": ".cab"
    },
    {
        "variation": 0,
        "hexLimit": 7,
        "magicNumber": "535A444488F02733",
        "extension": ".ex?, ? can be replaced by anything"
    },
    {
        "variation": 0,
        "hexLimit": 4,
        "magicNumber": "464C4946",
        "extension": ".flif"
    },
    {
        "variation": 0,
        "hexLimit": 4,
        "magicNumber": "1A45DFA3",
        "extension": ".mkv .mka .mks .mk3d .webm"
    },
    {
        "variation": 0,
        "hexLimit": 4,
        "magicNumber": "4D494C20",
        "extension": ".stg"
    },
    {
        "variation": 1,
        "hexLimit": 15,
        "magicNumber": "41542654464F524D????????444A56",
        "extension": ".djvu .djv"
    },
    {
        "variation": 0,
        "hexLimit": 2,
        "magicNumber": "3082",
        "extension": ".der"
    },
    {
        "variation": 0,
        "hexLimit": 4,
        "magicNumber": "4449434D",
        "extension": ".dcm"
    },
    {
        "variation": 0,
        "hexLimit": 4,
        "magicNumber": "774F4646",
        "extension": ".woff"
    },
    {
        "variation": 0,
        "hexLimit": 4,
        "magicNumber": "774F4632",
        "extension": ".woff2"
    },
    {
        "variation": 0,
        "hexLimit": 6,
        "magicNumber": "3c3f786d6c20",
        "extension": ".XML"
    },
    {
        "variation": 0,
        "hexLimit": 4,
        "magicNumber": "0061736d",
        "extension": ".wasm"
    },
    {
        "variation": 0,
        "hexLimit": 3,
        "magicNumber": "cf8401",
        "extension": "3"
    },
    {
        "variation": 0,
        "hexLimit": 3,
        "magicNumber": "435753",
        "extension": ".swf"
    },
    {
        "variation": 0,
        "hexLimit": 3,
        "magicNumber": "465753",
        "extension": ".swf"
    },
    {
        "variation": 0,
        "hexLimit": 7,
        "magicNumber": "213C617263683E",
        "extension": ".deb"
    },
    {
        "variation": 1,
        "hexLimit": 12,
        "magicNumber": "52494646????????57454250",
        "extension": ".webp"
    },
    {
        "variation": 0,
        "hexLimit": 4,
        "magicNumber": "27051956",
        "extension": "none, U-Boot / uImage. Das U-Boot Universal Boot Loader."
    },
    {
        "variation": 0,
        "hexLimit": 6,
        "magicNumber": "7B5C72746631",
        "extension": ".rtf"
    },
    {
        "variation": 0,
        "hexLimit": 4,
        "magicNumber": "54415045",
        "extension": "none, Microsoft Tape Format"
    },
    {
        "variation": 0,
        "hexLimit": 1,
        "magicNumber": "47",
        "extension": ".ts .tsv .tsa"
    },
    {
        "variation": 0,
        "hexLimit": 4,
        "magicNumber": "000001BA",
        "extension": ".m2p .vob"
    },
    {
        "variation": 0,
        "hexLimit": 4,
        "magicNumber": "000001BA",
        "extension": ".mpg .mpeg"
    },
    {
        "variation": 0,
        "hexLimit": 1,
        "magicNumber": "47",
        "extension": ".mpg .mpeg"
    },
    {
        "variation": 0,
        "hexLimit": 4,
        "magicNumber": "000001B3",
        "extension": ".mpg .mpeg"
    },
    {
        "variation": 0,
        "hexLimit": 2,
        "magicNumber": "7801",
        "extension": ".zlib"
    },
    {
        "variation": 0,
        "hexLimit": 2,
        "magicNumber": "789C",
        "extension": ".zlib"
    },
    {
        "variation": 0,
        "hexLimit": 2,
        "magicNumber": "78DA",
        "extension": ".zlib"
    },
    {
        "variation": 0,
        "hexLimit": 4,
        "magicNumber": "62767832",
        "extension": ".lzfse"
    },
    {
        "variation": 0,
        "hexLimit": 3,
        "magicNumber": "4F5243",
        "extension": ".orc"
    },
    {
        "variation": 0,
        "hexLimit": 4,
        "magicNumber": "4F626A01",
        "extension": ".avro"
    },
    {
        "variation": 0,
        "hexLimit": 4,
        "magicNumber": "53455136",
        "extension": ".rc"
    },
    {
        "variation": 0,
        "hexLimit": 4,
        "magicNumber": "65877856",
        "extension": ".p25 .obt"
    },
    {
        "variation": 0,
        "hexLimit": 4,
        "magicNumber": "5555aaaa",
        "extension": ".pcv"
    },
    {
        "variation": 0,
        "hexLimit": 3,
        "magicNumber": "785634",
        "extension": ".pbt .pdt .pea .peb .pet .pgt .pict .pjt .pkt .pmt"
    },
    {
        "variation": 0,
        "hexLimit": 4,
        "magicNumber": "50415231",
        "extension": "none, Apache Parquet columnar file format"
    },
    {
        "variation": 0,
        "hexLimit": 4,
        "magicNumber": "454D5832",
        "extension": ".ez2"
    },
    {
        "variation": 0,
        "hexLimit": 4,
        "magicNumber": "454D5533",
        "extension": ".ez3 .iso"
    },
    {
        "variation": 0,
        "hexLimit": 4,
        "magicNumber": "1B4C7561",
        "extension": ".luac"
    },
    {
        "variation": 0,
        "hexLimit": 16,
        "magicNumber": "626F6F6B000000006D61726B00000000",
        "extension": ".alias"
    },
    {
        "variation": 0,
        "hexLimit": 14,
        "magicNumber": "5B5A6F6E655472616E736665725D",
        "extension": ".identifier"
    },
    {
        "variation": 0,
        "hexLimit": 8,
        "magicNumber": "5265636569766564",
        "extension": ".eml"
    },
    {
        "variation": 0,
        "hexLimit": 12,
        "magicNumber": "20020162A01EAB0702000000",
        "extension": ".tde"
    },
    {
        "variation": 0,
        "hexLimit": 15,
        "magicNumber": "3748030200000000583530394B4559",
        "extension": ".kdb"
    },
    {
        "variation": 0,
        "hexLimit": 4,
        "magicNumber": "28B52FFD",
        "extension": ".zst"
    },
    {
        "variation": 0,
        "hexLimit": 3,
        "magicNumber": "3A290A",
        "extension": ".sml"
    }
]

os.system("clear")
print("Welcome to CheckFiler! \n")
testFile = raw_input("Enter the name of the file: ")
with open(testFile, 'rb') as f:
    content = f.read()
os.system("clear")
print("Printing the hex values of the script")
# print(binascii.hexlify(content))
for dictGrabber in listOf4HexValues:
    if dictGrabber.get("variation") == 0:
        limitGrab = dictGrabber.get("hexLimit") + 1
        hexGrab = dictGrabber.get("magicNumber").lower()
        grabbingLimit = 0
        grabbedHex = ""
        # import pdb
        # pdb.set_trace()
        while grabbingLimit < limitGrab:
            grabbedHex = grabbedHex + \
                binascii.hexlify(content[grabbingLimit])
            grabbingLimit = grabbingLimit + 1
            if grabbedHex == hexGrab:
                print("Found a match!")
                kindOfFile = dictGrabber.get("extension")
                print(kindOfFile)
                exit()
            else:
                continue
    elif dictGrabber.get("variation") == 1:
        # print("Skipping variation")
        if dictGrabber.get("hexLimit") >= 12:
            # print("This part will match")
        else:
            break
