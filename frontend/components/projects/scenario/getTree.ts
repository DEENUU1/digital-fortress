import {useEffect, useState} from "react";

export default function getTree(projectId: number) {
	// eslint-disable-next-line react-hooks/rules-of-hooks
	const [tree, setTree] = useState<ScenarioResponse[]>([]);

	// eslint-disable-next-line react-hooks/rules-of-hooks
	useEffect(() => {
		fetch(process.env.API_URL + `api/v1/scenario/tree/${projectId}`, {
			credentials: "include"
		})
			.then(response => response.json())
			.then(data => setTree(data));
	}, [projectId]);

	return tree
}