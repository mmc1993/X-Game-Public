// <auto-generated>
//   This file was generated by a tool; you should avoid making direct changes.
//   Consider using 'partial classes' to extend these types
//   Input: share.proto
// </auto-generated>

#pragma warning disable CS0612, CS1591, CS3021, IDE1006, RCS1036, RCS1057, RCS1085, RCS1192
namespace Protocol
{

    [global::ProtoBuf.ProtoContract(Name = @"vec3")]
    public partial class Vec3 : global::ProtoBuf.IExtensible
    {
        private global::ProtoBuf.IExtension __pbn__extensionData;
        global::ProtoBuf.IExtension global::ProtoBuf.IExtensible.GetExtensionObject(bool createIfMissing)
            => global::ProtoBuf.Extensible.GetExtensionObject(ref __pbn__extensionData, createIfMissing);

        [global::ProtoBuf.ProtoMember(1, Name = @"x")]
        public int X { get; set; }

        [global::ProtoBuf.ProtoMember(2, Name = @"y")]
        public int Y { get; set; }

        [global::ProtoBuf.ProtoMember(3, Name = @"z")]
        public int Z { get; set; }

    }

    [global::ProtoBuf.ProtoContract()]
    public partial class UserInfo : global::ProtoBuf.IExtensible
    {
        private global::ProtoBuf.IExtension __pbn__extensionData;
        global::ProtoBuf.IExtension global::ProtoBuf.IExtensible.GetExtensionObject(bool createIfMissing)
            => global::ProtoBuf.Extensible.GetExtensionObject(ref __pbn__extensionData, createIfMissing);

        [global::ProtoBuf.ProtoMember(1, Name = @"user_id")]
        public int UserId { get; set; }

        [global::ProtoBuf.ProtoMember(2, Name = @"slot_id")]
        public int SlotId { get; set; }

        [global::ProtoBuf.ProtoMember(3, Name = @"name")]
        [global::System.ComponentModel.DefaultValue("")]
        public string Name { get; set; } = "";

    }

}

#pragma warning restore CS0612, CS1591, CS3021, IDE1006, RCS1036, RCS1057, RCS1085, RCS1192
