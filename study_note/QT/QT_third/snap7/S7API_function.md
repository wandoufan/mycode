# snap7的client模式提供的API函数

备注：目前只用过DBRead和DBWrite，其他那么多函数没用过，也不知道用法

## 常用函数
1. S7Object S7API Cli_Create();

2. int S7API Cli_ConnectTo(S7Object Client, const char \*Address, int Rack, int Slot);

3. int S7API Cli_DBRead(S7Object Client, int DBNumber, int Start, int Size, void \*pUsrData);

4. int S7API Cli_DBWrite(S7Object Client, int DBNumber, int Start, int Size, void \*pUsrData);

5. int S7API Cli_GetConnected(S7Object Client, int \*Connected);
检查当前连接状态，Connected为1代表已连接，为0代表未连接  
```
int i = 10;
int *connected = &i;
int result = Cli_GetConnected(plc_client, connected);
cout << "result:" << result << endl;
cout << "connected:" << *connected << endl;
```


## S7Object的定义
```
// multi platform/processor object reference
// DON'T CONFUSE IT WITH AN OLE OBJECT, IT'S SIMPLY
// AN INTEGER VALUE (32 OR 64 BIT) USED AS HANDLE.
typedef uintptr_t  S7Object;
```


## 全部函数
```
S7Object S7API Cli_Create();
void S7API Cli_Destroy(S7Object *Client);
int S7API Cli_ConnectTo(S7Object Client, const char *Address, int Rack, int Slot);
int S7API Cli_SetConnectionParams(S7Object Client, const char *Address, word LocalTSAP, word RemoteTSAP);
int S7API Cli_SetConnectionType(S7Object Client, word ConnectionType);
int S7API Cli_Connect(S7Object Client);
int S7API Cli_Disconnect(S7Object Client);
int S7API Cli_GetParam(S7Object Client, int ParamNumber, void *pValue);
int S7API Cli_SetParam(S7Object Client, int ParamNumber, void *pValue);
int S7API Cli_SetAsCallback(S7Object Client, pfn_CliCompletion pCompletion, void *usrPtr);
// Data I/O main functions
int S7API Cli_ReadArea(S7Object Client, int Area, int DBNumber, int Start, int Amount, int WordLen, void *pUsrData);
int S7API Cli_WriteArea(S7Object Client, int Area, int DBNumber, int Start, int Amount, int WordLen, void *pUsrData);
int S7API Cli_ReadMultiVars(S7Object Client, PS7DataItem Item, int ItemsCount);
int S7API Cli_WriteMultiVars(S7Object Client, PS7DataItem Item, int ItemsCount);
// Data I/O Lean functions
int S7API Cli_DBRead(S7Object Client, int DBNumber, int Start, int Size, void *pUsrData);
int S7API Cli_DBWrite(S7Object Client, int DBNumber, int Start, int Size, void *pUsrData);
int S7API Cli_MBRead(S7Object Client, int Start, int Size, void *pUsrData);
int S7API Cli_MBWrite(S7Object Client, int Start, int Size, void *pUsrData);
int S7API Cli_EBRead(S7Object Client, int Start, int Size, void *pUsrData);
int S7API Cli_EBWrite(S7Object Client, int Start, int Size, void *pUsrData);
int S7API Cli_ABRead(S7Object Client, int Start, int Size, void *pUsrData);
int S7API Cli_ABWrite(S7Object Client, int Start, int Size, void *pUsrData);
int S7API Cli_TMRead(S7Object Client, int Start, int Amount, void *pUsrData);
int S7API Cli_TMWrite(S7Object Client, int Start, int Amount, void *pUsrData);
int S7API Cli_CTRead(S7Object Client, int Start, int Amount, void *pUsrData);
int S7API Cli_CTWrite(S7Object Client, int Start, int Amount, void *pUsrData);
// Directory functions
int S7API Cli_ListBlocks(S7Object Client, TS7BlocksList *pUsrData);
int S7API Cli_GetAgBlockInfo(S7Object Client, int BlockType, int BlockNum, TS7BlockInfo *pUsrData);
int S7API Cli_GetPgBlockInfo(S7Object Client, void *pBlock, TS7BlockInfo *pUsrData, int Size);
int S7API Cli_ListBlocksOfType(S7Object Client, int BlockType, TS7BlocksOfType *pUsrData, int *ItemsCount);
// Blocks functions
int S7API Cli_Upload(S7Object Client, int BlockType, int BlockNum, void *pUsrData, int *Size);
int S7API Cli_FullUpload(S7Object Client, int BlockType, int BlockNum, void *pUsrData, int *Size);
int S7API Cli_Download(S7Object Client, int BlockNum, void *pUsrData, int Size);
int S7API Cli_Delete(S7Object Client, int BlockType, int BlockNum);
int S7API Cli_DBGet(S7Object Client, int DBNumber, void *pUsrData, int *Size);
int S7API Cli_DBFill(S7Object Client, int DBNumber, int FillChar);
// Date/Time functions
int S7API Cli_GetPlcDateTime(S7Object Client, tm *DateTime);
int S7API Cli_SetPlcDateTime(S7Object Client, tm *DateTime);
int S7API Cli_SetPlcSystemDateTime(S7Object Client);
// System Info functions
int S7API Cli_GetOrderCode(S7Object Client, TS7OrderCode *pUsrData);
int S7API Cli_GetCpuInfo(S7Object Client, TS7CpuInfo *pUsrData);
int S7API Cli_GetCpInfo(S7Object Client, TS7CpInfo *pUsrData);
int S7API Cli_ReadSZL(S7Object Client, int ID, int Index, TS7SZL *pUsrData, int *Size);
int S7API Cli_ReadSZLList(S7Object Client, TS7SZLList *pUsrData, int *ItemsCount);
// Control functions
int S7API Cli_PlcHotStart(S7Object Client);
int S7API Cli_PlcColdStart(S7Object Client);
int S7API Cli_PlcStop(S7Object Client);
int S7API Cli_CopyRamToRom(S7Object Client, int Timeout);
int S7API Cli_Compress(S7Object Client, int Timeout);
int S7API Cli_GetPlcStatus(S7Object Client, int *Status);
// Security functions
int S7API Cli_GetProtection(S7Object Client, TS7Protection *pUsrData);
int S7API Cli_SetSessionPassword(S7Object Client, char *Password);
int S7API Cli_ClearSessionPassword(S7Object Client);
// Low level
int S7API Cli_IsoExchangeBuffer(S7Object Client, void *pUsrData, int *Size);
// Misc
int S7API Cli_GetExecTime(S7Object Client, int *Time);
int S7API Cli_GetLastError(S7Object Client, int *LastError);
int S7API Cli_GetPduLength(S7Object Client, int *Requested, int *Negotiated);
int S7API Cli_ErrorText(int Error, char *Text, int TextLen);
// 1.1.0
int S7API Cli_GetConnected(S7Object Client, int *Connected);
//------------------------------------------------------------------------------
//  Async functions
//------------------------------------------------------------------------------
int S7API Cli_AsReadArea(S7Object Client, int Area, int DBNumber, int Start, int Amount, int WordLen, void *pUsrData);
int S7API Cli_AsWriteArea(S7Object Client, int Area, int DBNumber, int Start, int Amount, int WordLen, void *pUsrData);
int S7API Cli_AsDBRead(S7Object Client, int DBNumber, int Start, int Size, void *pUsrData);
int S7API Cli_AsDBWrite(S7Object Client, int DBNumber, int Start, int Size, void *pUsrData);
int S7API Cli_AsMBRead(S7Object Client, int Start, int Size, void *pUsrData);
int S7API Cli_AsMBWrite(S7Object Client, int Start, int Size, void *pUsrData);
int S7API Cli_AsEBRead(S7Object Client, int Start, int Size, void *pUsrData);
int S7API Cli_AsEBWrite(S7Object Client, int Start, int Size, void *pUsrData);
int S7API Cli_AsABRead(S7Object Client, int Start, int Size, void *pUsrData);
int S7API Cli_AsABWrite(S7Object Client, int Start, int Size, void *pUsrData);
int S7API Cli_AsTMRead(S7Object Client, int Start, int Amount, void *pUsrData);
int S7API Cli_AsTMWrite(S7Object Client, int Start, int Amount, void *pUsrData);
int S7API Cli_AsCTRead(S7Object Client, int Start, int Amount, void *pUsrData);
int S7API Cli_AsCTWrite(S7Object Client, int Start, int Amount, void *pUsrData);
int S7API Cli_AsListBlocksOfType(S7Object Client, int BlockType, TS7BlocksOfType *pUsrData, int *ItemsCount);
int S7API Cli_AsReadSZL(S7Object Client, int ID, int Index, TS7SZL *pUsrData, int *Size);
int S7API Cli_AsReadSZLList(S7Object Client, TS7SZLList *pUsrData, int *ItemsCount);
int S7API Cli_AsUpload(S7Object Client, int BlockType, int BlockNum, void *pUsrData, int *Size);
int S7API Cli_AsFullUpload(S7Object Client, int BlockType, int BlockNum, void *pUsrData, int *Size);
int S7API Cli_AsDownload(S7Object Client, int BlockNum, void *pUsrData, int Size);
int S7API Cli_AsCopyRamToRom(S7Object Client, int Timeout);
int S7API Cli_AsCompress(S7Object Client, int Timeout);
int S7API Cli_AsDBGet(S7Object Client, int DBNumber, void *pUsrData, int *Size);
int S7API Cli_AsDBFill(S7Object Client, int DBNumber, int FillChar);
int S7API Cli_CheckAsCompletion(S7Object Client, int *opResult);
int S7API Cli_WaitAsCompletion(S7Object Client, int Timeout);
```