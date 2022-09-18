// <auto-generated>
//   This file was generated by a tool; you should avoid making direct changes.
//   Consider using 'partial classes' to extend these types
//   Input: rsp.proto
// </auto-generated>

#pragma warning disable CS0612, CS1591, CS3021, IDE1006, RCS1036, RCS1057, RCS1085, RCS1192
namespace Protocol
{

    [global::ProtoBuf.ProtoContract()]
    public partial class RspJoin : global::ProtoBuf.IExtensible
    {
        private global::ProtoBuf.IExtension __pbn__extensionData;
        global::ProtoBuf.IExtension global::ProtoBuf.IExtensible.GetExtensionObject(bool createIfMissing)
            => global::ProtoBuf.Extensible.GetExtensionObject(ref __pbn__extensionData, createIfMissing);

        [global::ProtoBuf.ProtoMember(1, Name = @"room_id")]
        public int RoomId { get; set; }

        [global::ProtoBuf.ProtoMember(2, Name = @"user_id")]
        public int UserId { get; set; }

        [global::ProtoBuf.ProtoMember(3, Name = @"main_id")]
        public int MainId { get; set; }

        [global::ProtoBuf.ProtoMember(4, Name = @"slot_id")]
        public int SlotId { get; set; }

        [global::ProtoBuf.ProtoMember(5, Name = @"map_id")]
        public int MapId { get; set; }

        [global::ProtoBuf.ProtoMember(6, Name = @"room_name")]
        [global::System.ComponentModel.DefaultValue("")]
        public string RoomName { get; set; } = "";

        [global::ProtoBuf.ProtoMember(7, Name = @"user_name")]
        [global::System.ComponentModel.DefaultValue("")]
        public string UserName { get; set; } = "";

        [global::ProtoBuf.ProtoMember(8, Name = @"other_users")]
        public global::System.Collections.Generic.List<UserInfo> OtherUsers { get; } = new global::System.Collections.Generic.List<UserInfo>();

    }

    [global::ProtoBuf.ProtoContract()]
    public partial class RspName : global::ProtoBuf.IExtensible
    {
        private global::ProtoBuf.IExtension __pbn__extensionData;
        global::ProtoBuf.IExtension global::ProtoBuf.IExtensible.GetExtensionObject(bool createIfMissing)
            => global::ProtoBuf.Extensible.GetExtensionObject(ref __pbn__extensionData, createIfMissing);

        [global::ProtoBuf.ProtoMember(1, Name = @"user_id")]
        public int UserId { get; set; }

        [global::ProtoBuf.ProtoMember(2, Name = @"user_name")]
        [global::System.ComponentModel.DefaultValue("")]
        public string UserName { get; set; } = "";

    }

    [global::ProtoBuf.ProtoContract()]
    public partial class RspRoomMap : global::ProtoBuf.IExtensible
    {
        private global::ProtoBuf.IExtension __pbn__extensionData;
        global::ProtoBuf.IExtension global::ProtoBuf.IExtensible.GetExtensionObject(bool createIfMissing)
            => global::ProtoBuf.Extensible.GetExtensionObject(ref __pbn__extensionData, createIfMissing);

        [global::ProtoBuf.ProtoMember(1, Name = @"user_id")]
        public int UserId { get; set; }

        [global::ProtoBuf.ProtoMember(2, Name = @"slot_n")]
        public int SlotN { get; set; }

        [global::ProtoBuf.ProtoMember(3, Name = @"map_id")]
        public int MapId { get; set; }

    }

    [global::ProtoBuf.ProtoContract()]
    public partial class RspEnterGameBeg : global::ProtoBuf.IExtensible
    {
        private global::ProtoBuf.IExtension __pbn__extensionData;
        global::ProtoBuf.IExtension global::ProtoBuf.IExtensible.GetExtensionObject(bool createIfMissing)
            => global::ProtoBuf.Extensible.GetExtensionObject(ref __pbn__extensionData, createIfMissing);

        [global::ProtoBuf.ProtoMember(1, Name = @"user_id")]
        public int UserId { get; set; }

    }

    [global::ProtoBuf.ProtoContract()]
    public partial class RspEnterGameEnd : global::ProtoBuf.IExtensible
    {
        private global::ProtoBuf.IExtension __pbn__extensionData;
        global::ProtoBuf.IExtension global::ProtoBuf.IExtensible.GetExtensionObject(bool createIfMissing)
            => global::ProtoBuf.Extensible.GetExtensionObject(ref __pbn__extensionData, createIfMissing);

        [global::ProtoBuf.ProtoMember(1, Name = @"srand_seed")]
        public int SrandSeed { get; set; }

        [global::ProtoBuf.ProtoMember(2, Name = @"time_stanp")]
        public long TimeStanp { get; set; }

        [global::ProtoBuf.ProtoMember(3, Name = @"sgame_addr")]
        [global::System.ComponentModel.DefaultValue("")]
        public string SgameAddr { get; set; } = "";

        [global::ProtoBuf.ProtoMember(4, Name = @"sgame_port")]
        public int SgamePort { get; set; }

    }

    [global::ProtoBuf.ProtoContract()]
    public partial class RspStartGame : global::ProtoBuf.IExtensible
    {
        private global::ProtoBuf.IExtension __pbn__extensionData;
        global::ProtoBuf.IExtension global::ProtoBuf.IExtensible.GetExtensionObject(bool createIfMissing)
            => global::ProtoBuf.Extensible.GetExtensionObject(ref __pbn__extensionData, createIfMissing);

        [global::ProtoBuf.ProtoMember(1, Name = @"time")]
        public int Time { get; set; }

    }

    [global::ProtoBuf.ProtoContract()]
    public partial class RspSetSlot : global::ProtoBuf.IExtensible
    {
        private global::ProtoBuf.IExtension __pbn__extensionData;
        global::ProtoBuf.IExtension global::ProtoBuf.IExtensible.GetExtensionObject(bool createIfMissing)
            => global::ProtoBuf.Extensible.GetExtensionObject(ref __pbn__extensionData, createIfMissing);

        [global::ProtoBuf.ProtoMember(1, Name = @"user_id")]
        public int UserId { get; set; }

        [global::ProtoBuf.ProtoMember(2, Name = @"new_slot_id")]
        public int NewSlotId { get; set; }

        [global::ProtoBuf.ProtoMember(3, Name = @"old_slot_id")]
        public int OldSlotId { get; set; }

    }

    [global::ProtoBuf.ProtoContract()]
    public partial class RspGetPort : global::ProtoBuf.IExtensible
    {
        private global::ProtoBuf.IExtension __pbn__extensionData;
        global::ProtoBuf.IExtension global::ProtoBuf.IExtensible.GetExtensionObject(bool createIfMissing)
            => global::ProtoBuf.Extensible.GetExtensionObject(ref __pbn__extensionData, createIfMissing);

        [global::ProtoBuf.ProtoMember(1, Name = @"port")]
        public int Port { get; set; }

    }

    [global::ProtoBuf.ProtoContract()]
    public partial class RspSetTeam : global::ProtoBuf.IExtensible
    {
        private global::ProtoBuf.IExtension __pbn__extensionData;
        global::ProtoBuf.IExtension global::ProtoBuf.IExtensible.GetExtensionObject(bool createIfMissing)
            => global::ProtoBuf.Extensible.GetExtensionObject(ref __pbn__extensionData, createIfMissing);

        [global::ProtoBuf.ProtoMember(1, Name = @"user_id")]
        public int UserId { get; set; }

        [global::ProtoBuf.ProtoMember(2, Name = @"team_flags")]
        public uint TeamFlags { get; set; }

    }

    [global::ProtoBuf.ProtoContract()]
    public partial class RspQuit : global::ProtoBuf.IExtensible
    {
        private global::ProtoBuf.IExtension __pbn__extensionData;
        global::ProtoBuf.IExtension global::ProtoBuf.IExtensible.GetExtensionObject(bool createIfMissing)
            => global::ProtoBuf.Extensible.GetExtensionObject(ref __pbn__extensionData, createIfMissing);

        [global::ProtoBuf.ProtoMember(1, Name = @"user_id")]
        public int UserId { get; set; }

    }

    [global::ProtoBuf.ProtoContract()]
    public partial class RspFrameData : global::ProtoBuf.IExtensible
    {
        private global::ProtoBuf.IExtension __pbn__extensionData;
        global::ProtoBuf.IExtension global::ProtoBuf.IExtensible.GetExtensionObject(bool createIfMissing)
            => global::ProtoBuf.Extensible.GetExtensionObject(ref __pbn__extensionData, createIfMissing);

        [global::ProtoBuf.ProtoMember(1, Name = @"frame")]
        public int Frame { get; set; }

    }

    [global::ProtoBuf.ProtoContract()]
    public partial class RspInit : global::ProtoBuf.IExtensible
    {
        private global::ProtoBuf.IExtension __pbn__extensionData;
        global::ProtoBuf.IExtension global::ProtoBuf.IExtensible.GetExtensionObject(bool createIfMissing)
            => global::ProtoBuf.Extensible.GetExtensionObject(ref __pbn__extensionData, createIfMissing);

        [global::ProtoBuf.ProtoMember(1, Name = @"token")]
        public int Token { get; set; }

    }

    [global::ProtoBuf.ProtoContract()]
    public partial class RspError : global::ProtoBuf.IExtensible
    {
        private global::ProtoBuf.IExtension __pbn__extensionData;
        global::ProtoBuf.IExtension global::ProtoBuf.IExtensible.GetExtensionObject(bool createIfMissing)
            => global::ProtoBuf.Extensible.GetExtensionObject(ref __pbn__extensionData, createIfMissing);

        [global::ProtoBuf.ProtoMember(1, Name = @"pid")]
        public int Pid { get; set; }

    }

}

#pragma warning restore CS0612, CS1591, CS3021, IDE1006, RCS1036, RCS1057, RCS1085, RCS1192