.. _data_encryption_permissions:

***********************
Permissions
***********************
Users with the appropriate encryption permission privilege's can encrypt and decrypt data.

**Comment** - *The rest of this content seems internal, correct?*

Implementation notes

one method to encrypt the data with is the TDE: Transparent data encryption  which employed by Microsoft/IBM/Oracle etc.

management. The requirement is that this will be programmatic via API.  

The centralized key management store should be one of the following (R&D to choose which one in accordance to easiness of deployment):

KMS (AWS)- https://aws.amazon.com/kms/

IBM- IBM Security Guardium Key Lifecycle Manager - Overview 