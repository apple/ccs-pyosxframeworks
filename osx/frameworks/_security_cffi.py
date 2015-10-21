##
# Copyright (c) 2015 Apple Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
##


INCLUDES = """
#include <Security/Security.h>
"""

EXTRA_LINKS = []

TYPES = """

// SecBase.h
typedef struct OpaqueSecCertificateRef *SecCertificateRef;
typedef struct OpaqueSecIdentityRef *SecIdentityRef;

// SecureTransport.h
typedef enum
{
    kSSLServerSide,
    kSSLClientSide
} SSLProtocolSide;

typedef enum
{
    kSSLStreamType,
    kSSLDatagramType
} SSLConnectionType;

typedef enum {
    kSSLProtocolUnknown = 0,                /* no protocol negotiated/specified; use default */
    kSSLProtocol3       = 2,                /* SSL 3.0 */
    kTLSProtocol1       = 4,                /* TLS 1.0 */
    kTLSProtocol11      = 7,                /* TLS 1.1 */
    kTLSProtocol12      = 8,                /* TLS 1.2 */
    kDTLSProtocol1      = 9,                /* DTLS 1.0 */

    /* DEPRECATED on iOS */
    kSSLProtocol2       = 1,                /* SSL 2.0 */
    kSSLProtocol3Only   = 3,                /* SSL 3.0 Only */
    kTLSProtocol1Only   = 5,                /* TLS 1.0 Only */
    kSSLProtocolAll     = 6,                /* All TLS supported protocols */

} SSLProtocol;

struct SSLContext;
typedef struct SSLContext *SSLContextRef;
typedef const void *SSLConnectionRef;

typedef OSStatus (*SSLReadFunc) ( SSLConnectionRef connection, void *data, size_t *dataLength );
typedef OSStatus (*SSLWriteFunc) ( SSLConnectionRef connection, const void *data, size_t *dataLength );
"""

CONSTANTS = """

// SecCertificateOIDs.h
const CFStringRef kSecOIDAuthorityInfoAccess;
const CFStringRef kSecOIDAuthorityKeyIdentifier;
const CFStringRef kSecOIDBasicConstraints;
const CFStringRef kSecOIDBiometricInfo;
const CFStringRef kSecOIDCSSMKeyStruct;
const CFStringRef kSecOIDCertIssuer;
const CFStringRef kSecOIDCertificatePolicies;
const CFStringRef kSecOIDClientAuth;
const CFStringRef kSecOIDCollectiveStateProvinceName;
const CFStringRef kSecOIDCollectiveStreetAddress;
const CFStringRef kSecOIDCommonName;
const CFStringRef kSecOIDCountryName;
const CFStringRef kSecOIDCrlDistributionPoints;
const CFStringRef kSecOIDCrlNumber;
const CFStringRef kSecOIDCrlReason;
const CFStringRef kSecOIDDeltaCrlIndicator;
const CFStringRef kSecOIDDescription;
const CFStringRef kSecOIDEmailAddress;
const CFStringRef kSecOIDEmailProtection;
const CFStringRef kSecOIDExtendedKeyUsage;
const CFStringRef kSecOIDExtendedKeyUsageAny;
const CFStringRef kSecOIDExtendedUseCodeSigning;
const CFStringRef kSecOIDGivenName;
const CFStringRef kSecOIDHoldInstructionCode;
const CFStringRef kSecOIDInvalidityDate;
const CFStringRef kSecOIDIssuerAltName;
const CFStringRef kSecOIDIssuingDistributionPoint;
const CFStringRef kSecOIDIssuingDistributionPoints;
const CFStringRef kSecOIDKeyUsage;
const CFStringRef kSecOIDLocalityName;
const CFStringRef kSecOIDMS_NTPrincipalName;
const CFStringRef kSecOIDMicrosoftSGC;
const CFStringRef kSecOIDNameConstraints;
const CFStringRef kSecOIDNetscapeCertSequence;
const CFStringRef kSecOIDNetscapeCertType;
const CFStringRef kSecOIDNetscapeSGC;
const CFStringRef kSecOIDOCSPSigning;
const CFStringRef kSecOIDOrganizationName;
const CFStringRef kSecOIDOrganizationalUnitName;
const CFStringRef kSecOIDPolicyConstraints;
const CFStringRef kSecOIDPolicyMappings;
const CFStringRef kSecOIDPrivateKeyUsagePeriod;
const CFStringRef kSecOIDQC_Statements;
const CFStringRef kSecOIDSerialNumber;
const CFStringRef kSecOIDServerAuth;
const CFStringRef kSecOIDStateProvinceName;
const CFStringRef kSecOIDStreetAddress;
const CFStringRef kSecOIDSubjectAltName;
const CFStringRef kSecOIDSubjectDirectoryAttributes;
const CFStringRef kSecOIDSubjectEmailAddress;
const CFStringRef kSecOIDSubjectInfoAccess;
const CFStringRef kSecOIDSubjectKeyIdentifier;
const CFStringRef kSecOIDSubjectPicture;
const CFStringRef kSecOIDSubjectSignatureBitmap;
const CFStringRef kSecOIDSurname;
const CFStringRef kSecOIDTimeStamping;
const CFStringRef kSecOIDTitle;
const CFStringRef kSecOIDUseExemptions;
const CFStringRef kSecOIDX509V1CertificateIssuerUniqueId;
const CFStringRef kSecOIDX509V1CertificateSubjectUniqueId;
const CFStringRef kSecOIDX509V1IssuerName;
const CFStringRef kSecOIDX509V1IssuerNameCStruct;
const CFStringRef kSecOIDX509V1IssuerNameLDAP;
const CFStringRef kSecOIDX509V1IssuerNameStd;
const CFStringRef kSecOIDX509V1SerialNumber;
const CFStringRef kSecOIDX509V1Signature;
const CFStringRef kSecOIDX509V1SignatureAlgorithm;
const CFStringRef kSecOIDX509V1SignatureAlgorithmParameters;
const CFStringRef kSecOIDX509V1SignatureAlgorithmTBS;
const CFStringRef kSecOIDX509V1SignatureCStruct;
const CFStringRef kSecOIDX509V1SignatureStruct;
const CFStringRef kSecOIDX509V1SubjectName;
const CFStringRef kSecOIDX509V1SubjectNameCStruct;
const CFStringRef kSecOIDX509V1SubjectNameLDAP;
const CFStringRef kSecOIDX509V1SubjectNameStd;
const CFStringRef kSecOIDX509V1SubjectPublicKey;
const CFStringRef kSecOIDX509V1SubjectPublicKeyAlgorithm;
const CFStringRef kSecOIDX509V1SubjectPublicKeyAlgorithmParameters;
const CFStringRef kSecOIDX509V1SubjectPublicKeyCStruct;
const CFStringRef kSecOIDX509V1ValidityNotAfter;
const CFStringRef kSecOIDX509V1ValidityNotBefore;
const CFStringRef kSecOIDX509V1Version;
const CFStringRef kSecOIDX509V3Certificate;
const CFStringRef kSecOIDX509V3CertificateCStruct;
const CFStringRef kSecOIDX509V3CertificateExtensionCStruct;
const CFStringRef kSecOIDX509V3CertificateExtensionCritical;
const CFStringRef kSecOIDX509V3CertificateExtensionId;
const CFStringRef kSecOIDX509V3CertificateExtensionStruct;
const CFStringRef kSecOIDX509V3CertificateExtensionType;
const CFStringRef kSecOIDX509V3CertificateExtensionValue;
const CFStringRef kSecOIDX509V3CertificateExtensionsCStruct;
const CFStringRef kSecOIDX509V3CertificateExtensionsStruct;
const CFStringRef kSecOIDX509V3CertificateNumberOfExtensions;
const CFStringRef kSecOIDX509V3SignedCertificate;
const CFStringRef kSecOIDX509V3SignedCertificateCStruct;
const CFStringRef kSecOIDSRVName;

// SecCertificate.h
const CFStringRef kSecPropertyKeyType;
const CFStringRef kSecPropertyKeyLabel;
const CFStringRef kSecPropertyKeyLocalizedLabel;
const CFStringRef kSecPropertyKeyValue;

CFStringRef kSecPropertyTypeWarning;
CFStringRef kSecPropertyTypeSuccess;
CFStringRef kSecPropertyTypeSection;
CFStringRef kSecPropertyTypeData;
CFStringRef kSecPropertyTypeString;
CFStringRef kSecPropertyTypeURL;
CFStringRef kSecPropertyTypeDate;
CFTypeRef kSecPropertyTypeTitle;
CFTypeRef kSecPropertyTypeError;

const CFStringRef kSecClass;

const CFStringRef kSecClassInternetPassword;
const CFStringRef kSecClassGenericPassword;
const CFStringRef kSecClassCertificate;
const CFStringRef kSecClassKey;
const CFStringRef kSecClassIdentity;

const CFStringRef kSecMatchPolicy;
const CFStringRef kSecMatchItemList;
const CFStringRef kSecMatchSearchList;
const CFStringRef kSecMatchIssuers;
const CFStringRef kSecMatchEmailAddressIfPresent;
const CFStringRef kSecMatchSubjectContains;
const CFStringRef kSecMatchSubjectStartsWith;
const CFStringRef kSecMatchSubjectEndsWith;
const CFStringRef kSecMatchSubjectWholeString;
const CFStringRef kSecMatchCaseInsensitive;
const CFStringRef kSecMatchDiacriticInsensitive;
const CFStringRef kSecMatchWidthInsensitive;
const CFStringRef kSecMatchTrustedOnly;
const CFStringRef kSecMatchValidOnDate;
const CFStringRef kSecMatchLimit;
const CFStringRef kSecMatchLimitOne;
const CFStringRef kSecMatchLimitAll;

const CFStringRef kSecReturnData;
const CFStringRef kSecReturnAttributes;
const CFStringRef kSecReturnRef;
const CFStringRef kSecReturnPersistentRef;

const CFStringRef kSecAttrAccessible;
const CFStringRef kSecAttrAccess;
const CFStringRef kSecAttrAccessControl;
const CFStringRef kSecAttrAccessGroup;
const CFStringRef kSecAttrSynchronizable;
const CFStringRef kSecAttrSynchronizableAny;
const CFStringRef kSecAttrCreationDate;
const CFStringRef kSecAttrModificationDate;
const CFStringRef kSecAttrDescription;
const CFStringRef kSecAttrComment;
const CFStringRef kSecAttrCreator;
const CFStringRef kSecAttrType;
const CFStringRef kSecAttrLabel;
const CFStringRef kSecAttrIsInvisible;
const CFStringRef kSecAttrIsNegative;
const CFStringRef kSecAttrAccount;
const CFStringRef kSecAttrService;
const CFStringRef kSecAttrGeneric;
const CFStringRef kSecAttrSecurityDomain;
const CFStringRef kSecAttrServer;
const CFStringRef kSecAttrProtocol;
const CFStringRef kSecAttrAuthenticationType;
const CFStringRef kSecAttrPort;
const CFStringRef kSecAttrPath;
const CFStringRef kSecAttrSubject;
const CFStringRef kSecAttrIssuer;
const CFStringRef kSecAttrSerialNumber;
const CFStringRef kSecAttrSubjectKeyID;
const CFStringRef kSecAttrPublicKeyHash;
const CFStringRef kSecAttrCertificateType;
const CFStringRef kSecAttrCertificateEncoding;
const CFStringRef kSecAttrKeyClass;
const CFStringRef kSecAttrApplicationLabel;
const CFStringRef kSecAttrIsPermanent;
const CFStringRef kSecAttrIsSensitive;
const CFStringRef kSecAttrIsExtractable;
const CFStringRef kSecAttrApplicationTag;
const CFStringRef kSecAttrKeyType;
const CFStringRef kSecAttrPRF;
const CFStringRef kSecAttrSalt;
const CFStringRef kSecAttrRounds;
const CFStringRef kSecAttrKeySizeInBits;
const CFStringRef kSecAttrEffectiveKeySize;
const CFStringRef kSecAttrCanEncrypt;
const CFStringRef kSecAttrCanDecrypt;
const CFStringRef kSecAttrCanDerive;
const CFStringRef kSecAttrCanSign;
const CFStringRef kSecAttrCanVerify;
const CFStringRef kSecAttrCanWrap;
const CFStringRef kSecAttrCanUnwrap;

const CFStringRef kSecValueData;
const CFStringRef kSecValueRef;
const CFStringRef kSecValuePersistentRef;

enum {
    errSSLProtocol                = -9800,    /* SSL protocol error */
    errSSLNegotiation            = -9801,    /* Cipher Suite negotiation failure */
    errSSLFatalAlert            = -9802,    /* Fatal alert */
    errSSLWouldBlock            = -9803,    /* I/O would block (not fatal) */
    errSSLSessionNotFound         = -9804,    /* attempt to restore an unknown session */
    errSSLClosedGraceful         = -9805,    /* connection closed gracefully */
    errSSLClosedAbort             = -9806,    /* connection closed via error */
    errSSLXCertChainInvalid     = -9807,    /* invalid certificate chain */
    errSSLBadCert                = -9808,    /* bad certificate format */
    errSSLCrypto                = -9809,    /* underlying cryptographic error */
    errSSLInternal                = -9810,    /* Internal error */
    errSSLModuleAttach            = -9811,    /* module attach failure */
    errSSLUnknownRootCert        = -9812,    /* valid cert chain, untrusted root */
    errSSLNoRootCert            = -9813,    /* cert chain not verified by root */
    errSSLCertExpired            = -9814,    /* chain had an expired cert */
    errSSLCertNotYetValid        = -9815,    /* chain had a cert not yet valid */
    errSSLClosedNoNotify        = -9816,    /* server closed session with no notification */
    errSSLBufferOverflow        = -9817,    /* insufficient buffer provided */
    errSSLBadCipherSuite        = -9818,    /* bad SSLCipherSuite */

    /* fatal errors detected by peer */
    errSSLPeerUnexpectedMsg        = -9819,    /* unexpected message received */
    errSSLPeerBadRecordMac        = -9820,    /* bad MAC */
    errSSLPeerDecryptionFail    = -9821,    /* decryption failed */
    errSSLPeerRecordOverflow    = -9822,    /* record overflow */
    errSSLPeerDecompressFail    = -9823,    /* decompression failure */
    errSSLPeerHandshakeFail        = -9824,    /* handshake failure */
    errSSLPeerBadCert            = -9825,    /* misc. bad certificate */
    errSSLPeerUnsupportedCert    = -9826,    /* bad unsupported cert format */
    errSSLPeerCertRevoked        = -9827,    /* certificate revoked */
    errSSLPeerCertExpired        = -9828,    /* certificate expired */
    errSSLPeerCertUnknown        = -9829,    /* unknown certificate */
    errSSLIllegalParam            = -9830,    /* illegal parameter */
    errSSLPeerUnknownCA         = -9831,    /* unknown Cert Authority */
    errSSLPeerAccessDenied        = -9832,    /* access denied */
    errSSLPeerDecodeError        = -9833,    /* decoding error */
    errSSLPeerDecryptError        = -9834,    /* decryption error */
    errSSLPeerExportRestriction    = -9835,    /* export restriction */
    errSSLPeerProtocolVersion    = -9836,    /* bad protocol version */
    errSSLPeerInsufficientSecurity = -9837,    /* insufficient security */
    errSSLPeerInternalError        = -9838,    /* internal error */
    errSSLPeerUserCancelled        = -9839,    /* user canceled */
    errSSLPeerNoRenegotiation    = -9840,    /* no renegotiation allowed */

    /* non-fatal result codes */
    errSSLPeerAuthCompleted     = -9841,    /* peer cert is valid, or was ignored if verification disabled */
    errSSLClientCertRequested    = -9842,    /* server has requested a client cert */

    /* more errors detected by us */
    errSSLHostNameMismatch        = -9843,    /* peer host name mismatch */
    errSSLConnectionRefused        = -9844,    /* peer dropped connection before responding */
    errSSLDecryptionFail        = -9845,    /* decryption failure */
    errSSLBadRecordMac            = -9846,    /* bad MAC */
    errSSLRecordOverflow        = -9847,    /* record overflow */
    errSSLBadConfiguration        = -9848,    /* configuration error */
    errSSLUnexpectedRecord      = -9849,    /* unexpected (skipped) record in DTLS */
    errSSLWeakPeerEphemeralDHKey = -9850,    /* weak ephemeral dh key  */

    /* non-fatal result codes */
    errSSLClientHelloReceived   = -9851,    /* SNI */
};
"""

FUNCTIONS = """

// SecCertificate.h
SecCertificateRef SecCertificateCopyPreferred(CFStringRef name, CFArrayRef keyUsage);
CFDictionaryRef SecCertificateCopyValues(SecCertificateRef certificate, CFArrayRef keys, CFErrorRef *error);

// SecIdentity.h
OSStatus SecIdentityCopyCertificate ( SecIdentityRef identityRef, SecCertificateRef *certificateRef );

// SecItem.h
OSStatus SecItemCopyMatching ( CFDictionaryRef query, CFTypeRef *result );

// SecKeychain.h
OSStatus SecKeychainSetUserInteractionAllowed ( Boolean state );

// SecureTransport.h
SSLContextRef
SSLCreateContext(CFAllocatorRef alloc, SSLProtocolSide protocolSide, SSLConnectionType connectionType);

OSStatus
SSLSetProtocolVersionEnabled (SSLContextRef     context,
                             SSLProtocol        protocol,
                             Boolean            enable);

OSStatus SSLSetConnection (SSLContextRef context, SSLConnectionRef connection);
OSStatus SSLGetConnection (SSLContextRef context, SSLConnectionRef *connection);

OSStatus SSLSetCertificate ( SSLContextRef context, CFArrayRef certRefs );
OSStatus SSLCopyPeerCertificates ( SSLContextRef context, CFArrayRef *certs );

OSStatus SSLSetIOFuncs ( SSLContextRef context, SSLReadFunc readFunc, SSLWriteFunc writeFunc );

OSStatus SSLHandshake ( SSLContextRef context );

OSStatus SSLWrite ( SSLContextRef context, const void *data, size_t dataLength, size_t *processed );
OSStatus SSLRead ( SSLContextRef context, void *data, size_t dataLength, size_t *processed );

OSStatus SSLClose ( SSLContextRef context );
"""
