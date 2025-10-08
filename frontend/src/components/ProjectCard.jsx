import React from "react";

function ProjectCard({ project }) {
  return (
    <div className="border rounded-xl p-4 shadow hover:shadow-lg transition">
      {project.image_url && (
        <img src={project.image_url} alt={project.title} className="rounded-lg mb-3" />
      )}
      <h2 className="font-semibold text-xl mb-2">{project.title}</h2>
      <p className="text-gray-600 mb-3">{project.description.slice(0, 120)}...</p>
      <div className="flex gap-4">
        {project.github_url && (
          <a href={project.github_url} target="_blank" className="text-blue-500 hover:underline">GitHub</a>
        )}
        {project.demo_url && (
          <a href={project.demo_url} target="_blank" className="text-green-500 hover:underline">Demo</a>
        )}
      </div>
    </div>
  );
}

export default ProjectCard;
