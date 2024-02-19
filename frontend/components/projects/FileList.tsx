import {toast} from "react-toastify";
import React, {useState, useEffect} from "react";
import {isConfigOption} from "jackspeak";
import {Modal, ModalContent, ModalHeader, ModalBody, ModalFooter, Button, useDisclosure} from "@nextui-org/react";
import ProjectStorageBar from "@/components/projects/ProjectStorageBar";


export default function FileList({projectId}: {projectId: number}){
	const { isOpen, onOpen, onClose } = useDisclosure();
	const [files, setFiles] = useState<FileResponse[]>([]);

	// eslint-disable-next-line react-hooks/exhaustive-deps
	const getFileList = async () => {
		try{
			const response = await fetch(process.env.API_URL + `/api/v1/file/${projectId}`,{
				method: "GET",
				headers: {
					"Content-Type": "application/json"
				},
				credentials: "include"
			});

			if (!response.ok){
				toast.error("Can't fetch list of files");
				return;
			}

			const data = await response.json();
			setFiles(data);

		} catch (error){
			toast.error("Error fetching list of files");
		}
	}


	useEffect(() => {
		if (isOpen){
			getFileList();
		}
	}, [getFileList, isOpen]);

  return (
    <>
      <Button onPress={onOpen}>Files</Button>
      <Modal
        size={"full"}
        isOpen={isOpen}
        onClose={onClose}
      >
        <ModalContent>
          {(onClose) => (
            <>
              <ModalHeader className="flex flex-col gap-1">Project files</ModalHeader>

              <ModalBody>
								{files.map((file) => (
									<div key={file.id} className="flex flex-col gap-1">
										<span>{file.file}</span>
									</div>
								))}
              </ModalBody>

              <ModalFooter>
                <Button color="danger" variant="light" onPress={onClose}>
                  Close
                </Button>
              </ModalFooter>
            </>
          )}
        </ModalContent>
      </Modal>
    </>
  );
}