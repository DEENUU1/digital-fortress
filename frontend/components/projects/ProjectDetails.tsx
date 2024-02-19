'use client';

import {Modal, ModalContent, ModalHeader, ModalBody, ModalFooter, Button, useDisclosure} from "@nextui-org/react";
import React, {useEffect, useState} from "react";
import {toast} from "react-toastify";
import {Table, TableHeader, TableColumn, TableBody, TableRow, TableCell} from "@nextui-org/react";
import ProjectStorageBar from "@/components/projects/ProjectStorageBar";

function TableData({project}: {project: ProjectResponse | null}){

	return (
		<Table isStriped aria-label="Example static collection table">
      <TableHeader>
        <TableColumn>LABEL</TableColumn>
        <TableColumn>DATA</TableColumn>
      </TableHeader>
      <TableBody>
				<TableRow key="1">
          <TableCell>Title</TableCell>
          <TableCell>{project?.title}</TableCell>
        </TableRow>
        <TableRow key="2">
          <TableCell>Current storage</TableCell>
          <TableCell>{project?.storage_usage}</TableCell>
        </TableRow>
				<TableRow key="3">
          <TableCell>Number of generated scenarios</TableCell>
          <TableCell>{project?.num_of_scenarios}</TableCell>
        </TableRow>
				<TableRow key="4">
          <TableCell>Created at</TableCell>
          <TableCell>{project?.created_at}</TableCell>
        </TableRow>
        <TableRow key="5">
          <TableCell>Updated at</TableCell>
          <TableCell>{project?.updated_at}</TableCell>
        </TableRow>
      </TableBody>
    </Table>
  );
}

export default function ProjectDetailsModal({ projectId }: { projectId: number }) {
  const { isOpen, onOpen, onClose } = useDisclosure();
  const [project, setProject] = useState<ProjectResponse | null>(null);

	const getProjectDetails = async () => {
    try {
      const response = await fetch(process.env.API_URL + `/api/v1/project/${projectId}`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
        credentials: "include"
      });

      if (!response.ok) {
        toast.error('Failed to fetch project details');
        return;
      }

      const data = await response.json();
      setProject(data);
    } catch (error) {
      toast.error('Error fetching project details');
    }
  };

  useEffect(() => {
    if (isOpen) {
      getProjectDetails();
    }
  }, [isOpen]);

  return (
    <>
      <Button onPress={onOpen}>Details</Button>
      <Modal
        size={"full"}
        isOpen={isOpen}
        onClose={onClose}
      >
        <ModalContent>
          {(onClose) => (
            <>
              <ModalHeader className="flex flex-col gap-1">Project details {project?.title}</ModalHeader>
              <ModalBody>
                <TableData project={project}/>
              </ModalBody>
              <ModalBody>
                <ProjectStorageBar value={+project?.storage_percentage}/>
                <strong>{project?.storage_percentage} %</strong>
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